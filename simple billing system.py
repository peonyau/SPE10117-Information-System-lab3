'''
Simple Billing System

Created on Nov 20, 2020

@author: tchan
'''
import fileinput
import sys

def displayFile(datafile):
    for line in fileinput.input(datafile):
        sys.stdout.write(line)

    
def main():
    instructions = """\nEnter one of the following:
        1 to print the contents of input transaction file
        2 to print all valid input transaction data
        3 to enter adjustment transaction
        4 to print customer report
        Q to end \n"""
    
       
    while True:
        sys.stdout.write(instructions) 
        sys.stdout.flush()      
        choice = input( "Enter 1 to 4 " ) 

        if choice == "1":
            displayFile(sys.argv[1])
        elif choice == "2":
            fileIn = open(sys.argv[1], 'r')

            data=[]
            
            lines = fileIn.read().splitlines()
            
            for line in lines:
                transactionRecord = line.split('_')

                if transactionRecord[2] != 'C' and transactionRecord[2] != 'D':      
                    sys.stderr.write('Invalid Transaction Code : ' + line + '\n')
                elif float(transactionRecord[3]) < 0 or float(transactionRecord[3]) > 100000 :      
                    sys.stderr.write('Invalid Transaction Amount: ' + line + '\n')
                else:    
                    data.append(transactionRecord)
                
            print('%-20s%-30s%5s%10s'%('Name','Address','Txn', 'Ampunt'))
            print('='*65)
            
            for e in data:
                print('%-20s%-30s%5s%10s'%(e[0], e[1], e[2], e[3]))

        elif choice == "3":
            customerName = input('Customer Name: ')
            transactionType = input('Transaction Type: ')
            transactionAmount = float(input('Transaction Amount: ') )

            i=0
            while i < len(clientDataList) and clientDataList[i]['Name'] != customerName:
                i += 1
            if i < len(clientDataList):
                if transactionType =='C':
                         clientDataList[i]['Balance'] -= transactionAmount
                     else:
                         clientDataList[i]['Balance'] += transactionAmount
            print('%-20s%-30s%10s'%('Name','Address','Balance'))
            print('='*60)
            for e in clientDataList:
                print('%-20s%-30s%10.2f'%(e['Name'],e['Address'],e['Balance']))                
                
        elif choice == "4":
            clientDataList = []
            for e in data:
                if len(clinentDataList) == 0:
                    if e[2] == 'C':
                       clinentDataList.append(dict(zip(['Name','Address','Balance'],
                                               [e[0],e[1],-float(e[3])])))
                    else:
                       clinentDataList.append(dict(zip(['Name','Address','Balance'],
                                               [e[0],e[1],float(e[3])])))
            else:
                 i=0
                 while i < len(clientDataList) and clientDataList[i]['Name'] != e[0]:
                     i += 1

                 if i == len(clientDataList):
                    if e[2] == 'C':
                       clinentDataList.append(dict(zip(['Name','Address','Balance'],
                                               [e[0],e[1],-float(e[3])])))
                    else:
                       clinentDataList.append(dict(zip(['Name','Address','Balance'],
                                               [e[0],e[1],float(e[3])])))
                 else:
                     if e[2] =='C':
                         clientDataList[i]['Balance'] -= float(e[3])
                     else:
                         clientDataList[i]['Balance'] += float(e[3])
            print('%-20s%-30s%10s'%('Name','Address','Balance'))
            print('='*60)
            for e in clientDataList:
                print('%-20s%-30s%10.2f'%(e['Name'],e['Address'],e['Balance']))
        elif choice == "Q":
            break

    print ("End Simple Billing System")

if __name__ == "__main__":
    sys.argv = [sys.argv[0],'datafile1.dat']
    displayFile(sys.argv[1])
    main()
