import numpy.random as r

adjective = ['a']*16
adjective[0] = 'pathetic,'
adjective[1] = 'pompous,' 
adjective[2] = 'jhola-wearing,' 
adjective[3] = 'corrupt,' 
adjective[4] = 'trotskyist,' 
adjective[5] = 'maoist,' 
adjective[6] = 'gay sex loving,'
adjective[7] = 'paki-loving,' 
adjective[8] = 'taliban sympathizing,'
adjective[9] = 'immoral,'
adjective[10] = 'weak,'
adjective[11] = 'sickular,'
adjective[12] = 'pseudo-secular,'
adjective[13] = 'videshi adulterated,'
adjective[14] = 'napunsak,'
adjective[15] = 'Ivory tower,'

anti = ['a']*6
anti[0] = 'anti-development' 
anti[1] = 'anti-progress' 
anti[2] = 'anti-Modi' 
anti[3] = 'anti-Indian' 
anti[4] = 'anti-national'
anti[5] = 'anti-Hindu'


adjective1 = ['a']*11
adjective1[0] = 'hippocrate'
adjective1[1] = 'fake-liberal'
adjective1[2] = 'bootlicking pacifist'
adjective1[3] = 'spineless'
adjective1[4] = 'contrarian' 
adjective1[5] = 'commie' 
adjective1[6] = 'naxalite' 
adjective1[7] = 'tree-hugging'
adjective1[8] = 'petition-signing'
adjective1[9] = 'dharna nautankibaaz'
adjective1[10] = 'naive'

hero = ['a']*40
hero[0] = 'faggot.' 
hero[1] = 'gay monkey.' 
hero[2] = 'troll.' 
hero[3] = 'gasbag.'
hero[4] = 'agitationist.' 
hero[5] = 'gay pedo.'
hero[6] = 'jihadi agent.' 
hero[7] = 'Vatican agent.' 
hero[8] = 'terrorist.' 
hero[9] = 'Tejpal-supporter.' 
hero[10] = 'Tehelka-subscriber.' 
hero[11] = 'commie tyrant.'
hero[12] = 'Italian ass-wipe.' 
hero[13] = 'Italian ass-licker.' 
hero[14] = 'dynasty-supporter.' 
hero[15] = 'congi scum.' 
hero[16] = 'fake liberal Fidayeen.'
hero[17] = 'Pappu-lover.'
hero[18] = 'minority-supporter.' 
hero[19] = 'minority-appeaser.'
hero[20] = 'fake Hindu.'
hero[21] = 'pathetic coward.'
hero[22] = 'Pappu ka chela.'
hero[23] = 'paid-news dalaal.'
hero[24] = 'Arundhati apologist.'
hero[25] = 'Fabindia libtard.'
hero[26] = 'Limo libtard.'
hero[27] = 'Shree 420 ka chela.'
hero[28] = 'AAPtard.'
hero[29] = 'Dawood-ka-chela.'
hero[30] = 'PR Ninja.'
hero[31] = 'congi dog.'
hero[32] = 'anarchist Kejri stooge.'
hero[33] = 'Khadi Bhandar liberal.'
hero[34] = 'eNREGA coolie.'
hero[35] = 'presstitute.'
hero[36] = 'false flag operative.'
hero[37] = 'fake victim blogposter.'
hero[38] = 'covert ops cyber-assassin.'
hero[39] = 'hidden agenda axegrinder.'

adj_len = len(adjective)
anti_len = len(anti)
adj1_len = len(adjective1)
hero_len = len(hero)

rand_adj = adjective[r.randint(0, high=adj_len)]
rand_anti = anti[r.randint(0, high=anti_len)]
rand_adj1 = adjective1[r.randint(0, high=adj1_len)]
rand_hero = hero[r.randint(0, high=hero_len)]


print(f'You {rand_adj} {rand_anti} {rand_adj1} {rand_hero}')

