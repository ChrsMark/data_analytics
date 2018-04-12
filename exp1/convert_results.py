
filename = "test_results_combination_R_rests.txt"
file = open(filename, "r")
for line in file:
   items = line.split('|')
   with open('results_R_converted_score.txt', 'a') as out:
       out.write("{}\t{}\t{}\n".format(items[0], items[1], items[2]))
   with open('results_R_converted_time.txt', 'a') as out:
       out.write("{}\t{}\t{}\n".format(items[0], items[1], items[3]))
