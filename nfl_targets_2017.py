import matplotlib as mpl

mpl.use('TkAgg')
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import seaborn as sns
import numpy as np
import warnings

warnings.filterwarnings('ignore')
sns.set_style("whitegrid")


class TeamTargets:

    def __init__(self):
        self.team_names = ['ravens', 'dolphins', 'cowboys', 'chargers', 'broncos', 'cardinals']
        self.team_abbrevs = ['BAL', 'MIA', 'DAL', 'LAC', 'DEN', 'ARI']

        self.team_dict = {}

        ravens_colours = ['xkcd:black', 'xkcd:black', 'xkcd:black', 'xkcd:purple', 'xkcd:purple', 'xkcd:purple',
                          'xkcd:purple', 'xkcd:purple', 'xkcd:purple']

        dolphins_colours = ['xkcd:orange', 'xkcd:aqua', 'xkcd:aqua', 'xkcd:orange', 'xkcd:aqua', 'xkcd:aqua',
                            'xkcd:aqua']

        cowboys_colours = ['xkcd:lightblue', 'xkcd:lightblue', 'xkcd:darkblue', 'xkcd:darkblue', 'xkcd:darkblue',
                           'xkcd:darkblue', 'xkcd:darkblue', 'xkcd:darkblue', 'xkcd:darkblue']

        chargers_colours = ['xkcd:azure', 'xkcd:goldenrod', 'xkcd:azure', 'xkcd:azure', 'xkcd:azure',
                            'xkcd:goldenrod', 'xkcd:goldenrod', 'xkcd:azure', 'xkcd:azure', 'xkcd:azure']

        broncos_colours = ['xkcd:orange', 'xkcd:orange', 'xkcd:blue', 'xkcd:blue', 'xkcd:blue', 'xkcd:orange',
                           'xkcd:blue', 'xkcd:orange', 'xkcd:orange', 'xkcd:orange', 'xkcd:orange', 'xkcd:orange',
                           'xkcd:orange']

        cardinals_colours = ['xkcd:red', 'xkcd:black', 'xkcd:red', 'xkcd:red', 'xkcd:black', 'xkcd:red',
                             'xkcd:red', 'xkcd:black', 'xkcd:red', 'xkcd:red', 'xkcd:red', 'xkcd:red']

        colour_dict = {'BAL': ravens_colours, 'MIA': dolphins_colours, 'DAL': cowboys_colours,
                       'LAC': chargers_colours, 'DEN': broncos_colours, 'ARI': cardinals_colours}
        official_name_dict = {'BAL': 'Baltimore Ravens', 'MIA': 'Miami Dolphins', 'DAL': 'Dallas Cowboys',
                              'LAC': 'Los Angeles Chargers', 'DEN': 'Denver Broncos', 'ARI': 'Arizona Cardinals'}

        for team, team_abbrev in zip(self.team_names, self.team_abbrevs):
            file = pd.read_csv(f'/Users/mattjohnson/PycharmProjects/nfltargets/teamTargets2017/{team}_targets_2017.csv')
            file.set_index('Player', inplace=True)
            t = Team(team_abbrev, team, colour_dict.get(team_abbrev), file, official_name_dict.get(team_abbrev))
            self.team_dict.update({team_abbrev: t})

    def plot_those_targets(self, team_abbrev):
        current_team = self.team_dict.get(team_abbrev)
        isinstance(current_team, Team)
        current_team.plot_targets()


###################  TEAM CLASS  #############################

class Team:

    def __init__(self, team_abbrev, team_name, colors, tgt_df, official_name):
        assert isinstance(team_abbrev, str)
        self.team_abbrev = team_abbrev
        self.team_name = team_name
        self.target_df = tgt_df
        self.colours = colors
        self.official_name = official_name
        self.legend_dict = {}
        self.colours_unique = list(set(self.colours))
        self.make_legend()

    def plot_targets(self):

        plt.subplots(figsize=(15, 7))

        ax = sns.barplot(x=self.target_df['TGT'].values, y=self.target_df.index, data=self.target_df,
                         palette=self.colours);

        legend_elements = [Patch(facecolor=self.legend_dict.get('Current'), edgecolor='black',
                                 label='Current Team Member'),
                           Patch(facecolor=self.legend_dict.get('Gone'), edgecolor='black',
                                 label='Departed')]

        ax.legend(handles=legend_elements, loc='right')

        for p in ax.patches:
            if np.isnan(p.get_width()):
                gh = 0.0
            else:
                gh = np.round(p.get_width(), 2)

            ax.annotate(int(gh), (np.round(gh + 0.25, 3), p.get_y() + 0.5))

        ax.set_title(f'Targets for the 2017 {self.official_name}')

        plt.show();

    def make_legend(self):

        for colour in ['xkcd:black', 'xkcd:blue', 'xkcd:lightblue', 'xkcd:orange', 'xkcd:goldenrod']:

            index_ = -1
            try:
                index_ = self.colours_unique.index(colour)
                self.legend_dict.update({'Gone': colour})
                self.legend_dict.update({'Current': self.colours_unique[(index_ + 1) % 2]})
            except ValueError:
                index_=index_

            if index_ >= 0:
                return
