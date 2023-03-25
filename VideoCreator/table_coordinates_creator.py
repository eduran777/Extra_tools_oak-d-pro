import csv

def formatC(cf):
    cf = cf[0:len(cf)-1]
    return float(cf)


def interp(c1n,c1w,c2n,c2w,num):
     c1n = formatC(c1n)
     c2n = formatC(c2n)
     c1w = formatC(c1w)
     c2w = formatC(c2w)

     cdn = (c2n -c1n)/num
     cdw = (c2w - c1w)/num
     coordinN = []
     coordinW = []
     for i in range(1,num+1):
         cfn = c1n +(cdn*i)
         cfw = c1w +(cdw*i)
         coordinN.append(cfn)
         coordinW.append(cfw)
     print("Coordenadas N ")
     print(coordinN)
     print("Coordenadas S ")
     print(coordinW)

     return (coordinN,coordinW)

with open('/Users/usuario/Documents/pruebas 03-03-2023/Cordeenadas /03162653.CSV','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(csv_reader)


    with open('/Users/usuario/Documents/pruebas 03-03-2023/Cordeenadas /Cordenadas intercep /coordenadasIntercept.CSV','w') as csv_new_file:
        csv_writer = csv.writer(csv_new_file)
        firstLine = ["INDEX","TAG","DATE","TIME","LATITUDE N/S","LONGITUDE E/W","HEIGHT","SPEED","HEADING"]
        csv_writer.writerow(firstLine)



        for i in range(1,len(rows)-1):
         print(len(rows[0]))
         csv_writer.writerow(rows[i])


         c1n = rows[i][4]
         c1w = rows[i][5]
         c2n = rows[i+1][4]
         c2w = rows[i+1][5]

         citerp = interp(c1n,c1w,c2n,c2w,3)

         print(citerp)
         print(citerp[0][1])

         print('New value rows:')
         linec1 = ["1","T","230303","162655",str(citerp[0][0])+"N",str(citerp[1][0])+"W","2630","32.5","22"]
         linec2 = ["1","T","230303","162655",str(citerp[0][1])+"N",str(citerp[1][1])+"W","2630","32.5","22"]
         print(linec1)
         print(linec2)
         csv_writer.writerow(linec1)
         csv_writer.writerow(linec2)



















































