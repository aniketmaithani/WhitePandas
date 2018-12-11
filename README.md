# WhitePandas

## Sample Program based on the following problem statement

- [!Problem Statement](https://docs.google.com/document/d/1HaJ_pDOle8B0fvncN2UTh5-WgrcAmQeax8TBjkg5Y_c/edit)


## How to ? 

- The following program tries to take csv file as input with the following fields : [event_name,time_to_expire,priority]
- csv file is then sorted based on `priority` and `time_to_expire`
- To run type `python processed_task.py abc.csv 2018-12-10 9:40`
- Where arg[1] is filename.csv
- arg[2] is datetime in following format YYYY-MM-DD H:M 

### Installation and Depedencies 
- In order to run this program make sure you have `Python3` on your system. 
- In order to install requirement run `pip install -r requirements.txt`
- For development install `dev-requirements.txt`

## ToDo's 
- Better Error Handling
- Enhanced Test Cases 
- Better Modularity

### Assumptions 
- All dates are defined in the following format : `YYYY-MM-DD H:M`


### Anything In Master Should Be Always Deployable

- In case you find any mistake with the code make sure to raise a PR. I'll be happy to contribute on this problem statement during my free time. 

### Total Time Spent [WAKATIME] : 1 hour 15 mins
