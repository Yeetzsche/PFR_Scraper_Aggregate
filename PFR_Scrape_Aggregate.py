import os
import pandas as pd, os

from PFR_Scrape_Dict import teams,teams2,adv_type,team_conv,months
from PFR_Scrape_Dict import AdvPlayerDefHeaders,AdvPlayerPassHeaders,AdvPlayerRecHeaders
from PFR_Scrape_Dict import AdvPlayerRushHeaders,PlayerDefHeaders,PlayerOffHeaders
from PFR_Scrape_Dict import SnapCountHeaders,KickHeaders,ReturnHeaders
from PFR_Scrape_Dict import teams,teams2,team_conv,months
from PFR_Scrape_Dict import adv_sch,adv_years,adv_type
from PFR_Scrape_Dict import AdvPlayerDefHeaders,AdvPlayerPassHeaders,AdvPlayerRecHeaders
from PFR_Scrape_Dict import AdvPlayerRushHeaders,PlayerDefHeaders,PlayerOffHeaders
from PFR_Scrape_Dict import SnapCountHeaders,KickHeaders,ReturnHeaders,Head_struct

def buildWidgetHTMLs(year):
    #building team widget htmls
    sch_url = []
    for i in teams:
        url_int = 'https://widgets.sports-reference.com/wg.fcgi?css=1&site=pfr&url=%2Fteams%2F' + i + '%2F' + str(year)+ '.htm&div=div_games'
        sch_url.insert(0,url_int)
        
    return sch_url

def readWidgetHTMLs(sch_url):
    #reading team widget htmls
    df_sch = []       
    for i in sch_url:
        dflist = pd.read_html(i)
        df_sch.append(dflist)
    
    return df_sch #return schedule

def buildSchedule(year):
    sch_url = buildWidgetHTMLs(year)
    df_sch = readWidgetHTMLs(sch_url)
    #pulling out team schedules

    idx = 30
    df_sch[idx+1][0].insert(8, 'Team', teams[0])
    dd= df_sch[idx+1][0][df_sch[idx+1][0].columns[[0,2,8,9,10]]]

    for i in range(1,32):
        df_sch[idx][0].insert(8, 'Team', teams[i])
        dd = dd.append(df_sch[idx][0][df_sch[idx][0].columns[[0,2,8,9,10]]])
        idx = idx-1
    
    dd.columns = range(dd.shape[1])
    dd.columns = ['Week','Date','Team','Home','Opp']

    return dd

def convertDates(dd,year):
    dates = dd['Date']
    dates.sort_index()
    dlist = []
    for i in dates:
        m = i.split(' ', 1)[0]
        m = months[m]
        d = i.split(' ', 1)[1]
        if len(d) < 2:
            d = '0'+d
        if m == '01':
            dlist.append(str(year+1) + m + d)
        else:
            dlist.append(str(year) + m + d)
        
    dd = dd.drop(['Date'], axis=1)
    dd.insert(1,'Date',dlist)
    return dd
    
def buildWidgetBoxScore(year):
    dd = buildSchedule(year)
    
    #building widget urls for boxscores
    url_df = pd.DataFrame()
    matchup_df = pd.DataFrame()
    
    #sort dataframe by only home games
    dd = dd[dd['Home'].isna()]
    
    #remove bye weeks
    dd = dd[dd.Opp != 'Bye Week']
    dd = convertDates(dd,year)
    dd = dd.sort_values(by=['Date'])
    
    for index, row in dd.iterrows():

        dum_day = row['Date']
        dum_opp = row['Opp']
        dum_home = row['Team']

        int_opp = team_conv[dum_opp]
            
        dum_url = pd.DataFrame()
        dum_matchup = pd.DataFrame()
        
        for j in adv_type:
                    
            url_int = 'https://widgets.sports-reference.com/wg.fcgi?css=1&site=pfr&url=%2Fboxscores%2F' + dum_day + '0' + dum_home +'.htm&div=div_' + j
            m_int = dum_day + '_' + j + '_' + dum_home + 'v' + int_opp
                
            dum_url[j] = [url_int]
            match_lbl = j + '_label'
            dum_matchup[match_lbl] = [m_int]
                
        url_df = url_df.append(dum_url)
        matchup_df = matchup_df.append(dum_matchup)
    
    #resetting index so dfs can be joined
    dd.reset_index(drop=True, inplace=True)
    url_df.reset_index(drop=True, inplace=True)
    matchup_df.reset_index(drop=True, inplace=True)
    
    dd = dd.join(url_df)
    dd = dd.join(matchup_df)

    return dd

def readData(**kwargs):
    """Webscraper to scrape all available box score game data provided by 
    Pro Football Reference (PFR)
    
    Parameters
    ----------
    year : The season of which you wish to collect data.

    week : The week you wish to collect data on or up to.
        
    multiple_weeks : True = collect all weeks up to the given week specified.
                     False = collect data only for given week.
    
    Returns
    -------
    None
    
    Outputs
    -------
    A folder containing all found tables on PFR's website for given box scores
    converted to individual .csv files
    """    
    year = int(kwargs.get('year', None))
    week = int(kwargs.get('week', None))
    multiple_weeks = kwargs.get('multiple_weeks', None)
    
    dd = buildWidgetBoxScore(year)
    
    head = dd.columns.values.tolist()
    head = [i for i in head if i not in ('Week','Date','Team','Home','Opp',
    'passing_advanced_label','rushing_advanced_label', 'receiving_advanced_label', 
    'defense_advanced_label', 'player_offense_label', 'player_defense_label', 
    'home_snap_counts_label','vis_snap_counts_label', 'kicking_label', 'returns_label'
    )]
    
    label_head = dd.columns.values.tolist()
    label_head = [i for i in label_head if i not in ('Week','Date','Team','Home','Opp',
    'passing_advanced','rushing_advanced', 'receiving_advanced', 
    'defense_advanced', 'player_offense', 'player_defense', 
    'home_snap_counts','vis_snap_counts', 'kicking', 'returns'
    )]
    
    team_head = dd.columns.values.tolist()
    team_head = [i for i in team_head if i not in ('Date','Home',
    'passing_advanced_label','rushing_advanced_label', 'receiving_advanced_label', 
    'defense_advanced_label', 'player_offense_label', 'player_defense_label', 
    'home_snap_counts_label','vis_snap_counts_label', 'kicking_label', 'returns_label',
    'passing_advanced','rushing_advanced', 'receiving_advanced', 
    'defense_advanced', 'player_offense', 'player_defense', 
    'home_snap_counts','vis_snap_counts', 'kicking', 'returns'
    )]
    
    if multiple_weeks is None:
        multiple_weeks = False
    
    if (multiple_weeks == True) & (week != 1):
        pull_weeks = list(range(1,week+1))
            
    else:
        pull_weeks = [week]
    
    df_int = dd[dd['Week'].isin(pull_weeks)]
    
    for index, row in df_int.iterrows():
        lbl_hd_it = 0
        enter_print = True
        for h in head:

            try:
                df1 = pd.DataFrame(pd.read_html(row[h])[0])
            except:
                print('Tables not found for: ', h)
            else:
                df1 = pd.DataFrame(pd.read_html(row[h])[0])
                
                print('Pulling data for: ', row[label_head[lbl_hd_it]])
                #Adding Headers
                if h == ('passing_advanced'):
                    df1.columns = AdvPlayerPassHeaders
                elif h == ('defense_advanced'):
                    df1.columns = AdvPlayerDefHeaders
                elif h == ('rushing_advanced'):
                    df1.columns = AdvPlayerRushHeaders
                elif h == ('receiving_advanced'):
                    df1.columns = AdvPlayerRecHeaders
                elif h == ('player_offense'):
                    df1.columns = PlayerOffHeaders
                elif h == ('player_defense'):
                    df1.columns = PlayerDefHeaders
                elif h == ('home_snap_counts'):
                    df1.columns = SnapCountHeaders
                    df1.insert(2,'Tm',row[team_head[1]])
                    df2 = df1
                elif h == ('vis_snap_counts'):
                    df1.columns = SnapCountHeaders
                    df1.insert(2,'Tm',team_conv[row[team_head[2]]])
                    df1 = df2.append(df1)
                elif h == ('kicking'):
                    df1.columns = KickHeaders
                elif h == ('returns'):
                    df1.columns = ReturnHeaders
                    
                if (h != 'home_snap_counts') & (h != 'vis_snap_counts'):
                    df1 = df1[df1.Player != 'Player'] #gets rid of header row separating teams
                    df1 = df1.dropna(subset=['Player'])
                    enter_print = True
                elif h == ('vis_snap_counts'):
                    enter_print = True
                else:
                    enter_print = False
                
                if enter_print == True:
                    outdir = './nfl_data' + '/' + str(year) + '/week' + str(row[team_head[0]]) +'/all_tables/'
                    if not os.path.isdir(outdir):
                        os.makedirs(outdir)
                        print('new folder path created: ', outdir)
                        
                    df1 = df1.replace(teams, teams2)
                    t = row[label_head[lbl_hd_it]] + 'data.csv'
                    csv_title = os.path.join(outdir, t)  
          
                    pd.DataFrame(df1).to_csv(csv_title)
                
            lbl_hd_it += 1
    print('Table scraping complete for week',row[team_head[0]])
            
def build_df(year, week):
    count = 0
    count2 = 0
    
    for w in range(1,week+1):
        t_path =  './nfl_data' + '/' + str(year) + '/week' + str(w) +'/all_tables'
        t_list = os.listdir(t_path)
        
        count = 0
        weekCount = 1

        for i in t_list:
            statSplit = i.split('_')
            gameDate = statSplit[0]

            fileRead = t_path + '/' + i 
            df = pd.read_csv(fileRead)
        
            #Add column of game date
            df["Date"] = gameDate
            teams = df.Tm.unique()
            df['Tm'] = df['Tm'].str.upper()
            #Adding column of opponents
            for j in teams:
                if (len(teams) > 1):
                    if (j == teams[0]):
                        df.loc[df.Tm == j,"Opp"] = teams[1]
                    else:
                        df.loc[df.Tm == j,"Opp"] = teams[0]
                
            df = df.fillna(0)
            df = df.drop(['Unnamed: 0'], axis=1)
            df = df.astype(str)
                
            if count2 > 0:
                merge_key = df_int.columns.intersection(df.columns)
                merge_key = merge_key.tolist()
                #Make sure each column is data type string
                    
                #create an intermediate dataframe of all new data
                dz = (df_int.merge(df, on=merge_key, how='left', indicator=True)
                         .query('_merge == "left_only"')
                         .drop('_merge', 1))
                #merge intermediate dataframe with printable dataframe
                df_int = pd.merge(df_int,df, on=merge_key, how='outer')
                #drop duplicates if they are duplicated in both name and team (this helps with teams with players of similar names)
                df_int = dz.append(df_int).drop_duplicates(subset=['Player','Tm'],keep = 'first')
            
            else:    
                oldDate = gameDate
                df_int = df
            count2 += 1
            
        count += 1
        if w == week:
            for col in df_int.columns:
                if (col != 'Player') & (col != 'Tm') & (col != 'Position'):
                    df_int[col].values[:] = 0
            df_empty = df_int    
            
    return df_empty

            

def buildAggregate(year,week):
    """A database Aggregator that works in concert with the PFR webscraper tool 
    Pro Football Reference (PFR)
    
    Parameters
    ----------
    year : The season of which you wish to collect data.

    week : The week you wish to collect data on or up to.
    
    Returns
    -------
    None
    
    Outputs
    -------
    A single .csv file that aggregates all weekly stat data provided by PFR
    """   
    for w in range(1,week+1):
        t_path =  './nfl_data' + '/' + str(year) + '/week' + str(w) +'/all_tables'
        t_list = os.listdir(t_path)
        
        df_shell = build_df(year, week)
        count = 0
        weekCount = 1
        
        print('Polling all tables to intelligently build shell df...')
        df_shell = df_shell.set_index(['Player','Tm'])

        for i in t_list:
            print('Reading in: ',i)
            statSplit = i.split('_')
            gameDate = statSplit[0]

            fileRead = t_path + '/' + i 
            df = pd.read_csv(fileRead)
            
            df = df.drop(['Unnamed: 0'], axis=1)
            df['Tm'] = df['Tm'].str.upper()
        
            
            teams = df.Tm.unique()
            df["Date"] = gameDate
            
            for j in teams:
                if (len(teams) > 1):
                    if (j == teams[0]):
                        df.loc[df.Tm == j,"Opp"] = teams[1]
                    else:
                        df.loc[df.Tm == j,"Opp"] = teams[0]
            
            df = df.fillna(0)
            df = df.set_index(['Player','Tm'])
            df = df.astype(str)
            df = df[~df.index.duplicated()]
            if count > 0:
                #update pre-allocated df_int with new data
                df_int.update(df)
        
            else:
                #only enter here if it is the first sheet of a week
                oldDate = gameDate
                df_int = df_shell
                df_int.update(df)

            count =+ 1
            

        df_int=df_int.reset_index()
        df_int=df_int[Head_struct]
        df_int = df_int.sort_values(['Tm', 'Position','Player'], ascending=[True, True, True])
        df_int = df_int.reset_index(drop=True)
        t = './nfl_data' + '/' + str(year) + '/week' + str(w) +'/CompiledData_week'+ str(w) + '.csv'
        pd.DataFrame(df_int).to_csv(t)
        pprint = 'Week' + str(w) + " Aggregated .csv complete."
        print()