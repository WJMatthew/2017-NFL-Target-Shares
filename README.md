
# Targets to Spare:  
## A Look at the Teams in the NFL Missing the Most Targets from the 2017 Season
#### Matthew Johnson, Sept 6, 2018
**Teams:**<br>
- Miami Dolphins
- Dallas Cowboys
- Baltimore Ravens
- Arizona Cardinals
- Los Angeles Chargers
- Denver Broncos


```python
import nfl_targets_2017 as nt
%load_ext autoreload
%autoreload 2
%matplotlib inline
tgts = nt.TeamTargets()
```

![Image](http://content.sportslogos.net/logos/7/150/thumbs/15073062018.gif)

## Miami Dolphins
**Target % Lost:**  46% <br>
**Targets potentially up for grabs:**  233 <br>
**Departures:** Jarvis Landry, Julius Thomas <br>
**New Additions:**  Danny Amendola (WR), Albert Wilson (WR), Mike Gesicki (TE)  <br>


```python
tgts.plot_those_targets('MIA')
```


![png](https://github.com/WJMatthew/2017-NFL-Target-Shares/blob/master/missing_targets/output_3_0.png)


![Image](http://content.sportslogos.net/logos/7/165/thumbs/406.gif)

## Dallas Cowboys
**Target % Lost:**  50% <br>
**Targets potentially up for grabs:** 230  <br>
**Departures:** Dez Bryant (WR), Jason Witten (TE) <br>
**New Additions:**  Allen Hurns (WR)  <br>


```python
tgts.plot_those_targets('DAL')
```


![png](https://github.com/WJMatthew/2017-NFL-Target-Shares/blob/master/missing_targets/output_5_0.png)


![Image](http://content.sportslogos.net/logos/7/153/thumbs/318.gif)

## Baltimore Ravens
**Target % Lost:** 60%  <br>
**Targets potentially up for grabs:** 266  <br>
**Departures:**  Mike Wallace (WR, 105), Ben Watson (TE, 89), Jeremy Maclin (WR, 72)<br>
**New Additions:** Michael Crabtree, John Brown <br>


```python
tgts.plot_those_targets('BAL')
```


![png](https://github.com/WJMatthew/2017-NFL-Target-Shares/blob/master/missing_targets/output_7_0.png)


![Image](http://content.sportslogos.net/logos/7/177/thumbs/kwth8f1cfa2sch5xhjjfaof90.gif)

## Arizona Cardinals
**Target % Lost:** 28%  <br>
**Targets potentially up for grabs:** 157  <br>
**Departures:** Jaron Brown (WR, 74), John Brown (WR, 59), Troy Niklas (TE, 24) <br>
**New Additions:**  Brice Butler (WR), Christian Kirk (WR) <br>


```python
tgts.plot_those_targets('ARI')
```


![png](https://github.com/WJMatthew/2017-NFL-Target-Shares/blob/master/missing_targets/output_9_0.png)


![Image](http://content.sportslogos.net/logos/7/6446/thumbs/644624152017.gif)

## Los Angeles Chargers
**Target % Lost:** 33%  <br>
**Targets potentially up for grabs:** 236  <br>
**Departures:** Antonio Gates (56, TE), Dontrelle Inman (WR, 54) <br>
**Injuries:** Hunter Henry (124, TE) <br>
**New Additions:** Virgil Green (TE) <br>


```python
tgts.plot_those_targets('LAC')
```


![png](https://github.com/WJMatthew/2017-NFL-Target-Shares/blob/master/missing_targets/output_11_0.png)


![Image](http://content.sportslogos.net/logos/7/161/thumbs/9ebzja2zfeigaziee8y605aqp.gif)

## Denver Broncos
**Target % Lost:** 32%  <br>
**Targets potentially up for grabs:** 178  <br>
**Departures:** Bennie Fowler (WR, 62), A.J. Derby (TE, 44), C.J. Anderson (RB, 41), Cody Latimer (WR, 31) <br>
**New Additions:** Royce Freeman (RB) <br>


```python
tgts.plot_those_targets('DEN')
```


![png](https://github.com/WJMatthew/2017-NFL-Target-Shares/blob/master/missing_targets/output_13_0.png)

