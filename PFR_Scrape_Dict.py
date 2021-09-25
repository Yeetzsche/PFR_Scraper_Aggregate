adv_sch = [
    '2000', '2001', '2002', '2003',
    '2004', '2005', '2006', '2007',
    '2008', '2009', '2010', '2011',
    '2012', '2013', '2014', '2015',
    '2016', '2017', '2018', '2019',
    '2020','2021'
]

adv_years = [
    '2018', '2019', '2020','2021'
]

teams = [
    'buf', 'nwe', 'mia', 'nyj',
    'pit', 'rav', 'cle', 'cin',
    'was', 'dal', 'nyg', 'phi',
    'chi', 'gnb', 'det', 'min',
    'jax', 'oti', 'clt', 'htx',
    'kan', 'rai', 'sdg', 'den',
    'nor', 'atl', 'car', 'tam',
    'crd', 'ram', 'sea', 'sfo'
]

teams2 = ['BUF', 'NWE', 'MIA', 'NYJ',
          'PIT', 'BAL', 'CLE', 'CIN',
          'WAS', 'DAL', 'NYG', 'PHI',
          'CHI', 'GNB', 'DET', 'MIN',
          'JAX', 'TEN', 'IND', 'HOU',
          'KAN', 'LVR', 'LAC', 'DEN',
          'NOR', 'ATL', 'CAR', 'TAM',
          'ARI', 'LAR', 'SEA', 'SFO'
          ]

adv_type =[
    'passing_advanced','rushing_advanced', 'receiving_advanced', 
    'defense_advanced', 'player_offense', 'player_defense', 
    'home_snap_counts','vis_snap_counts', 'kicking', 'returns'
]

team_conv = { 'New England Patriots' : 'nwe',
    'New York Jets' : 'nyj',
    'Miami Dolphins' : 'mia',
    'Buffalo Bills' : 'buf',
    'Pittsburgh Steelers' : 'pit', 
    'Baltimore Ravens' : 'rav', 
    'Cleveland Browns' : 'cle', 
    'Cincinnati Bengals' : 'cin',
    'Washington Football Team' : 'was', 
    'Dallas Cowboys' : 'dal', 
    'New York Giants' : 'nyg', 
    'Philadelphia Eagles' : 'phi',
    'Chicago Bears' : 'chi', 
    'Green Bay Packers' : 'gnb', 
    'Detroit Lions' : 'det', 
    'Minnesota Vikings' : 'min',
    'Jacksonville Jaguars' : 'jax', 
    'Tennessee Titans' : 'oti', 
    'Indianapolis Colts' : 'clt', 
    'Houston Texans' : 'htx',
    'Kansas City Chiefs' : 'kan', 
    'Las Vegas Raiders' : 'rai', 
    'Los Angeles Chargers' : 'sdg', 
    'Denver Broncos' : 'den',
    'New Orleans Saints' : 'nor', 
    'Atlanta Falcons' : 'atl', 
    'Carolina Panthers' : 'car', 
    'Tampa Bay Buccaneers' : 'tam',
    'Arizona Cardinals' : 'crd', 
    'Los Angeles Rams' : 'ram', 
    'Seattle Seahawks' : 'sea', 
    'San Francisco 49ers' : 'sfo'
}

months = { 'January' : '01',
          'February' : '02',
          'March' : '03',
          'April' : '04',
          'May' : '05', 
          'June' : '06',
          'July' : '07',
          'August' : '08',
          'September' : '09',
          'October' : '10',
          'November' : '11',
          'December' : '12'
}


AdvPlayerDefHeaders = ['Player' , 'Tm', 'DefInt', 'DefTgt', 'DefCmp', 'DefCmp%', 'DefAllowYds', 'DefYds/Cmp', 
                    'DefYds/Tgt', 'DefAllowTD', 'DefAllowPassRating', 'DefDADOT','DefAir','DefAllowYAC', 'DefBlitz', 'DefQBHrry',
                    'DefQBKD', 'DefSk', 'DefPrss','DefCombo','DefMTKI','DefMTKI%']
AdvPlayerPassHeaders = ['Player' , 'Tm', 'PassCmp', 'PassAtt', 'PassYds', 'Pass1D', 'Pass1D%', 'PassIAY', 
                    'PassIAY/PA', 'PassCAY', 'PassCAY/Cmp', 'PassCAY/PA','PassYAC','PassYAC/Cmp', 'PassDropPass', 'PassDropPass%',
                    'PassBadTh', 'PassBad%', 'PassSk','PassBlitz','PassHrry','PassHit','PassPrss','PassPrss%','PassScrm','PassYds/Scr']

AdvPlayerRecHeaders = ['Player' , 'Tm', 'Re_Tgt', 'Re_Rec', 'Re_Yds','Re_TD', 'Re_1D',
                    'Re_YBC', 'Re_YBC/R', 'Re_YAC', 'Re_YAC/R','Re_ADOT','Re_BrkTkl', 'Rec/Br', 'Re_Drop', 'Re_DropPass%',
                    'Re_Int', 'Re_PassRating']

AdvPlayerRushHeaders = ['Player', 'Tm','R_Att', 'R_Yds', 'R_1D',
                       'R_YBC', 'R_YBC/Att', 'R_YAC', 'R_YAC/Att','R_BrkTkl', 'R_Att/Br']

PlayerDefHeaders = ['Player' , 'Tm', 'DefInt', 'DefIntYrds', 'DefIntTD', 'DefIntLng', 
                    'DefPD', 'DefSk', 'DefCombo', 'DefSolo','DefAst','DefTFL', 'DefQBHit', 'DefFR',
                    'Defyds', 'DefTD', 'DefFF']

PlayerOffHeaders = ['Player' , 'Tm', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'PassInt', 
                    'PassSk', 'PassYds/Cmp', 'PassLng', 'PassRate', 'R_Att', 'R_Yds', 
                    'R_TD', 'R_Lng', 'Re_Tgt', 'Re_Rec', 'Re_Yds', 'Re_TD',
                    'Re_Lng', 'Re_Fmb', 'Re_Fl']

SnapCountHeaders = ['Player' , 'Position', 'OffNum', 'Off%', 'DefNum', 'Def%', 
                    'STNum', 'ST%']

KickHeaders = ['Player' , 'Tm', 'XPM', 'XPA', 'FGM', 'FGA', 
                    'Pnt#', 'Pnt_yds','Pnt_Y/P','Pnt_Lng']

ReturnHeaders = ['Player' , 'Tm', 'KR#', 'KR_Yds', 'KR_Y/R', 'KR_TD', 
                    'KR_Lng', 'PR#','PR_Yds', 'PR_Y/R', 'PR_TD','PR_Lng' ]

Head_struct = ['Player', 'Tm', 'Position', 'OffNum', 'Off%', 'DefNum', 'Def%', 
               'STNum', 'ST%','PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'PassInt','PassYds/Cmp', 'PassLng', 'PassRate', 
               'Pass1D', 'Pass1D%', 'PassIAY', 'PassIAY/PA', 'PassCAY', 'PassCAY/Cmp', 'PassCAY/PA','PassYAC','PassYAC/Cmp', 
               'PassDropPass', 'PassDropPass%', 'PassBadTh', 'PassBad%', 'PassSk','PassBlitz','PassHrry','PassHit','PassPrss',
               'PassPrss%','PassScrm','PassYds/Scr','R_Att', 'R_Yds','R_TD', 'R_Lng', 'R_1D','R_YBC', 'R_YBC/Att', 'R_YAC', 
               'R_YAC/Att','R_BrkTkl', 'R_Att/Br', 'Re_Tgt', 'Re_Rec', 'Re_Yds', 'Re_TD', 'Re_Lng', 'Re_Fmb', 'Re_Fl',
               'Re_1D', 'Re_YBC', 'Re_YBC/R', 'Re_YAC', 'Re_YAC/R','Re_ADOT','Re_BrkTkl', 'Rec/Br', 'Re_Drop', 'Re_DropPass%',
               'Re_Int', 'Re_PassRating','DefInt', 'DefIntYrds', 'DefIntTD', 'DefIntLng','DefPD', 'DefSk', 'DefCombo', 
               'DefSolo','DefAst','DefTFL', 'DefQBHit', 'DefFR', 'Defyds', 'DefTD', 'DefFF', 'DefTgt','DefCmp', 'DefCmp%', 
               'DefAllowYds', 'DefYds/Cmp', 'DefYds/Tgt', 'DefAllowTD', 'DefAllowPassRating', 'DefDADOT','DefAir','DefAllowYAC', 
               'DefBlitz', 'DefQBHrry','DefQBKD', 'DefPrss','DefMTKI','DefMTKI%','KR#', 'KR_Yds', 'KR_Y/R', 'KR_TD', 'KR_Lng', 
               'PR#','PR_Yds', 'PR_Y/R', 'PR_TD','PR_Lng', 'XPM', 'XPA', 'FGM', 'FGA', 'Pnt#', 'Pnt_yds','Pnt_Y/P','Pnt_Lng'
               ]
