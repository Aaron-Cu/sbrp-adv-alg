import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

### Number of vertices
num_vertices = 88

### Adjacent list
graph = {"1" : [["2", 4], ["6", 1], ["7", 2], ["26", 2], ["34", 3]],
         "2" : [["1", 4]],
         "3" : [["4", 1], ["12", 1]],
         "4" : [["3", 1], ["9", 1]],
         "5" : [["6", 1], ["9", 1]],
         "6" : [["1", 6], ["5", 1], ["7", 3], ["26", 2]],
         "7" : [["1", 2], ["6", 3], ["8", 1], ["26", 3]],
         "8" : [["7", 1]],
         "9" : [["4", 1], ["5", 1], ["10", 1]],
         "10" : [["9", 1], ["11", 1]],
         "11" : [["10", 1], ["12", 1]], 
         "12" : [["3", 1], ["11", 1]],
         "13" : [["14", 2]],
         "14" : [["13", 2] , ["19", 2], ["91", 2]], 
         "15" : [["16", 1], ["17", 1], ["18", 1]],
         "16" : [["15", 1], ["17", 1]],
         "17" : [["15", 1], ["16", 1], ["18", 1]],
         "18" : [["15", 1], ["17", 1], ["19", 1]],
         "19" : [["14", 2], ["18", 1], ["20", 2], ["21", 2], ["87", 3], ["91", 3]],
         "20" : [["19", 2], ["21", 1], ["87", 2]],
         "21" : [["19", 2], ["20", 1], ["87", 2]],
         "22" : [["23", 1], ["63", 2], ["81", 1], ["88", 2]],
         "23" : [["22", 1], ["24", 4]],
         "24" : [["18", 1], ["23", 4], ["25", 2], ["33", 2], ["78", 1]],
         "25" : [["24", 2], ["33", 1], ["34", 1]],
         "26" : [["1", 2], ["6", 2], ["7", 3], ["27", 1], ["34", 2]],
         "27" : [["26", 1], ["28", 1]],
         "28" : [["27, 1"], ["62", 2]], 
         "29" : [["58", 1], ["59", 3], ["60", 3]],
         "30" : [["31", 1], ["32", 2], ["33", 2], ["46", 1], ["34", 3]],
         "31" : [["30", 1]],
         "32" : [["30", 2], ["33", 2], ["46", 2]],
         "33" : [["24", 4], ["25", 3], ["30", 2], ["32", 2], ["46", 3]], 
         "34" : [["1", 3], ["25", 1], ["26", 2], ["30", 3]],
         "35" : [["36", 1], ["40", 1]],
         "36" : [["35", 1], ["37", 1]],
         "37" : [["36", 1], ["38", 1]],
         "38" : [["37", 1], ["39", 1]],
         "39" : [["38", 1], ["40", 1]],
         "40" : [["35", 1], ["39", 1]],
         "41" : [["42", 1], ["56", 3], ["57", 2]],
         "42" : [["41", 1], ["43", 1]],
         "43" : [["42", 1], ["44", 4]],
         "44" : [["43", 4], ["45", 3]],
         "45" : [["44", 3]],
         "46" : [["30", 2], ["32", 3], ["33", 3] , ["47", 1], ["52", 1]],
         "47" : [["46", 1], ["48", 1], ["50", 2], ["52", 2]],
         "48" : [["47", 1], ["49", 1], ["50", 2], ["53", 1]],
         "49" : [["48", 1], ["50", 1], ["53", 1]], 
         "50" : [["47", 2], ["48", 2], ["49", 1], ["51", 1]],
         "51" : [["50", 1], ["52", 1]],
         "52" : [["46", 1], ["47", 1], ["51", 1]],
         "53" : [["48", 1], ["49", 1], ["54", 1]],
         "54" : [["53", 1], ["56", 1]],
         "55" : [["56", 1]],
         "57" : [["41", 2], ["56", 1], ["58", 1]],
         "58" : [["57", 1]],
         "59" : [["60", 2]],
         "60" : [["59", 2], ["61", 1]], 
         "61" : [["60", 1], ["62", 1]],
         "62" : [["28", 2], ["61", 1]],
         "63" : [["22", 2], ["64", 1], ["66", 1], ["67", 1]],
         "64" : [["63", 1], ["65", 1], ["66", 1]],
         "65" : [["64", 1], ["66", 1], ["71", 1], ["72", 1]],
         "66" : [["63", 1], ["64", 1], ["65", 1], ["67", 1], ["68", 1], ["71", 1]],
         "67" : [["63", 1], ["66", 1], ["68", 1]],
         "68" : [["66", 1], ["67", 1], ["69", 1], ["70", 1], ["71", 1]],
         "69" : [["68", 1], ["70", 1], ["71", 1]],
         "70" : [["68", 1], ["69", 1], ["71", 1]],
         "71" : [["65", 1], ["66", 1], ["68", 1], ["69", 1], ["70", 1], ["72", 1]],
         "72" : [["65", 1], ["71", 1], ["73", 2]],
         "73" : [["72", 2], ["76", 2]],
         "74" : [["75", 1]],
         "75" : [["74", 1], ["76", 1]],
         "76" : [["73", 2], ["77", 1]],
         "77" : [["76", 1], ["78", 1]],
         "78" : [["24", 1], ["77", 1]],
         "79" : [["80", 2], ["82", 3]],
         "80" : [["79", 2], ["82", 3]],
         "81" : [["22", 1], ["82", 1]],
         "82" : [["79", 3], ["80", 3], ["81", 1]],
         "83" : [["84", 1], ["85", 1], ["87", 4]],
         "84" : [["83", 1], ["85", 1]],
         "85" : [["83", 1], ["84", 1], ["87", 3]],
         "86" : [["87", 1]],
         "87" : [["85", 3], ["86", 1]],          
         "91" : [["14", 2] , ["19", 2], ["1", 3]]
         }


### Distance to school





### Visualization of graph
G = nx.Graph()


### Create an adjacent list of a graph using dictionary
G.add_edge("0", "1", weight=0)

G.add_edge("0", "18", weight=0)
G.add_edge("0", "19", weight=0)

G.add_edge("0", "24", weight=0)
G.add_edge("0", "25", weight=0)
G.add_edge("0", "62_1", weight=0)
G.add_edge("0", "26", weight=0)
G.add_edge("0", "6", weight=0)



G.add_edge("1", "2", weight=0)
G.add_edge("1", "7", weight=0)
G.add_edge("1", "26", weight=0)
G.add_edge("1", "62_1", weight=0)

G.add_edge("2", "1", weight=0)

G.add_edge("3", "4", weight=0)
G.add_edge("3", "12", weight=0)

G.add_edge("4", "3", weight=0)
G.add_edge("4", "9", weight=0)

G.add_edge("5", "6", weight=0)
G.add_edge("5", "9", weight=0)

G.add_edge("6", "1", weight=0)
G.add_edge("6", "5", weight=0) 
G.add_edge("6", "7", weight=0)  
G.add_edge("6", "26", weight=0)   
G.add_edge("6", "62_1", weight=0)

G.add_edge("7", "1", weight=0)
G.add_edge("7", "6", weight=0)
G.add_edge("7", "8", weight=0)  
G.add_edge("7", "26", weight=0)   
G.add_edge("7", "62_1", weight=0)

G.add_edge("8", "7", weight=0)

G.add_edge("9", "4", weight=0)
G.add_edge("9", "5", weight=0)
G.add_edge("9", "10", weight=0) 

G.add_edge("10", "9", weight=0)
G.add_edge("10", "11", weight=0)    

G.add_edge("11", "10", weight=0)
G.add_edge("11", "12", weight=0)    

G.add_edge("12", "3", weight=0)
G.add_edge("12", "11", weight=0)

G.add_edge("13", "14", weight=0)

G.add_edge("14", "13", weight=0)
G.add_edge("14", "19", weight=0)
G.add_edge("14", "91", weight=0)

G.add_edge("15", "16", weight=0)
G.add_edge("15", "17", weight=0)
G.add_edge("15", "18", weight=0)

G.add_edge("16", "15", weight=0)
G.add_edge("16", "17", weight=0)

G.add_edge("17", "15", weight=0)
G.add_edge("17", "16", weight=0)    
G.add_edge("17", "18", weight=0)

G.add_edge("18", "15", weight=0)
G.add_edge("18", "17", weight=0)    
G.add_edge("18", "19", weight=0)

G.add_edge("19", "14", weight=0)
G.add_edge("19", "18", weight=0)    
G.add_edge("19", "20", weight=0)    
G.add_edge("19", "21", weight=0)
G.add_edge("19", "87", weight=0)
G.add_edge("19", "91", weight=0)

G.add_edge("20", "19", weight=0)
G.add_edge("20", "21", weight=0)    
G.add_edge("20", "87", weight=0)

G.add_edge("21", "19", weight=0)
G.add_edge("21", "20", weight=0)    
G.add_edge("21", "87", weight=0)

G.add_edge("22", "23", weight=0)
G.add_edge("22", "63", weight=0)
G.add_edge("22", "81", weight=0)
G.add_edge("22", "88", weight=0)

G.add_edge("23", "22", weight=0)
G.add_edge("23", "24", weight=0)

G.add_edge("24", "18", weight=0)
G.add_edge("24", "23", weight=0)
G.add_edge("24", "25", weight=0) 
G.add_edge("24", "33", weight=0)
G.add_edge("24", "63", weight=0)

G.add_edge("25", "24", weight=0)    
G.add_edge("25", "33", weight=0)
G.add_edge("25", "62_1", weight=0)

G.add_edge("26", "1", weight=0)
G.add_edge("26", "6", weight=0)
G.add_edge("26", "7", weight=0) 
G.add_edge("26", "27", weight=0)    
G.add_edge("26", "62_1", weight=0)

G.add_edge("27", "26", weight=0)    
G.add_edge("27", "28", weight=0)

G.add_edge("28", "27", weight=0)    
G.add_edge("28", "62", weight=0)

G.add_edge("29", "58", weight=0)
G.add_edge("29", "92", weight=0)

G.add_edge("30", "31", weight=0)
G.add_edge("30", "32", weight=0)
G.add_edge("30", "33", weight=0)
G.add_edge("30", "46", weight=0)

G.add_edge("31", "30", weight=0)

G.add_edge("32", "30", weight=0)
G.add_edge("32", "33", weight=0)
G.add_edge("32", "46", weight=0)

G.add_edge("33", "24", weight=0)
G.add_edge("33", "25", weight=0)    
G.add_edge("33", "30", weight=0)
G.add_edge("33", "32", weight=0)    
G.add_edge("33", "46", weight=0)

G.add_edge("35", "36", weight=0)
G.add_edge("35", "40", weight=0)

G.add_edge("36", "35", weight=0)
G.add_edge("36", "37", weight=0)

G.add_edge("37", "36", weight=0)    
G.add_edge("37", "38", weight=0)    

G.add_edge("38", "37", weight=0)    
G.add_edge("38", "39", weight=0)

G.add_edge("39", "38", weight=0)    
G.add_edge("39", "40", weight=0)    
G.add_edge("39", "94", weight=0)

G.add_edge("40", "35", weight=0)
G.add_edge("40", "39", weight=0)    

G.add_edge("41", "42", weight=0)
G.add_edge("41", "56", weight=0)
G.add_edge("41", "57", weight=0)

G.add_edge("42", "41", weight=0)
G.add_edge("42", "43", weight=0)

G.add_edge("43", "42", weight=0)
G.add_edge("43", "44", weight=0)

G.add_edge("44", "43", weight=0)
G.add_edge("44", "45", weight=0)    

G.add_edge("45", "44", weight=0)

G.add_edge("46", "30", weight=0)
G.add_edge("46", "32", weight=0)
G.add_edge("46", "33", weight=0)
G.add_edge("46", "47", weight=0)
G.add_edge("46", "52", weight=0)

G.add_edge("47", "46", weight=0)
G.add_edge("47", "48", weight=0)
G.add_edge("47", "52", weight=0)

G.add_edge("48", "47", weight=0)
G.add_edge("48", "49", weight=0)
G.add_edge("48", "50", weight=0)
G.add_edge("48", "53", weight=0)

G.add_edge("49", "48", weight=0)
G.add_edge("49", "50", weight=0)
G.add_edge("49", "53", weight=0)

G.add_edge("50", "47", weight=0)
G.add_edge("50", "48", weight=0)
G.add_edge("50", "49", weight=0)
G.add_edge("50", "51", weight=0)

G.add_edge("51", "50", weight=0)
G.add_edge("51", "52", weight=0)

G.add_edge("52", "46", weight=0)
G.add_edge("52", "47", weight=0)
G.add_edge("52", "51", weight=0)

G.add_edge("53", "48", weight=0)
G.add_edge("53", "49", weight=0)
G.add_edge("53", "54", weight=0)

G.add_edge("54", "53", weight=0)
G.add_edge("54", "56", weight=0)

G.add_edge("55", "56", weight=0)

G.add_edge("56", "41", weight=0)
G.add_edge("56", "54", weight=0)
G.add_edge("56", "55", weight=0)
G.add_edge("56", "57", weight=0)

G.add_edge("57", "41", weight=0)
G.add_edge("57", "56", weight=0)
G.add_edge("57", "58", weight=0)

G.add_edge("58", "57", weight=0)

G.add_edge("59", "60", weight=0)

G.add_edge("60", "59", weight=0)
G.add_edge("60", "61", weight=0)

G.add_edge("61", "60", weight=0)
G.add_edge("61", "62", weight=0)

G.add_edge("62", "28", weight=0)
G.add_edge("62", "61", weight=0)

G.add_edge("62_1", "1", weight=0)
G.add_edge("62_1", "6", weight=0)
G.add_edge("62_1", "7", weight=0)
G.add_edge("62_1", "25", weight=0)
G.add_edge("62_1", "26", weight=0)
G.add_edge("62_1", "30", weight=0)


G.add_edge("63", "22", weight=0)
G.add_edge("63", "64", weight=0)
G.add_edge("63", "66", weight=0)
G.add_edge("63", "67", weight=0)

G.add_edge("64", "63", weight=0)
G.add_edge("64", "65", weight=0)
G.add_edge("64", "66", weight=0)

G.add_edge("65", "64", weight=0)
G.add_edge("65", "66", weight=0)
G.add_edge("65", "71", weight=0)
G.add_edge("65", "72", weight=0)

G.add_edge("66", "63", weight=0)
G.add_edge("66", "64", weight=0)
G.add_edge("66", "65", weight=0)
G.add_edge("66", "67", weight=0)
G.add_edge("66", "68", weight=0)
G.add_edge("66", "71", weight=0)


G.add_edge("67", "63", weight=0)
G.add_edge("67", "66", weight=0)
G.add_edge("67", "68", weight=0)

G.add_edge("68", "66", weight=0)
G.add_edge("68", "67", weight=0)
G.add_edge("68", "69", weight=0)
G.add_edge("68", "70", weight=0)
G.add_edge("68", "71", weight=0)

G.add_edge("69", "68", weight=0)
G.add_edge("69", "70", weight=0)
G.add_edge("69", "71", weight=0)

G.add_edge("70", "68", weight=0)
G.add_edge("70", "69", weight=0)
G.add_edge("70", "71", weight=0)

G.add_edge("71", "65", weight=0)
G.add_edge("71", "66", weight=0)
G.add_edge("71", "68", weight=0)
G.add_edge("71", "69", weight=0)
G.add_edge("71", "70", weight=0)
G.add_edge("71", "72", weight=0)

G.add_edge("72", "65", weight=0)
G.add_edge("72", "71", weight=0)
G.add_edge("72", "73", weight=0)

G.add_edge("73", "72", weight=0)
G.add_edge("73", "76", weight=0)

G.add_edge("74", "75", weight=0)

G.add_edge("75", "76", weight=0)

G.add_edge("76", "73", weight=0)
G.add_edge("76", "77", weight=0)

G.add_edge("77", "76", weight=0)
G.add_edge("77", "78", weight=0)

G.add_edge("78", "24", weight=0)
G.add_edge("78", "77", weight=0)

G.add_edge("79", "80", weight=0)
G.add_edge("79", "82", weight=0)

G.add_edge("80", "79", weight=0)
G.add_edge("80", "82", weight=0)

G.add_edge("81", "22", weight=0)
G.add_edge("81", "82", weight=0)

G.add_edge("82", "79", weight=0)
G.add_edge("82", "80", weight=0)
G.add_edge("82", "81", weight=0)


G.add_edge("83", "84", weight=0)
G.add_edge("83", "85", weight=0)
G.add_edge("83", "87", weight=0)

G.add_edge("84", "83", weight=0)
G.add_edge("84", "85", weight=0)

G.add_edge("85", "83", weight=0)
G.add_edge("85", "84", weight=0)
G.add_edge("85", "87", weight=0)

G.add_edge("86", "87", weight=0)

G.add_edge("87", "85", weight=0)
G.add_edge("87", "86", weight=0)


pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility
# nodes
nx.draw_networkx_nodes(G, pos)
# edges
nx.draw_networkx_edges(G, pos)
# node labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
ax = plt.gca()
#ax.margins(0.08)
#plt.axis("off")
#plt.tight_layout()
plt.show()