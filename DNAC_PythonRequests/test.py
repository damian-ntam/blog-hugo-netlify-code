import requests
from authenticate import get_token
from pprint import pprint

def main(): 
   d = {
      'audi': {'POOR': 12, 'FAIR': 40, 'GOOD': 20}, 
      'bmw': {'POOR': 0, 'FAIR': 42, 'GOOD': 22}
   }
   print(d)
   calculatePercentage(d)

def calculatePercentage(d):
   #Calculate Totals
   sum_audi = 0
   for key, value in d['audi'].items():
      sum_audi += value
   
   sum_bmw = 0
   for key, value in d['bmw'].items():
      sum_bmw += value
  
   #Calculate Percentages
   for key, value in d.items():
      if key == 'audi':
         print(f"Sum_audi: {sum_audi}")
         for k, v in value.items():
            percentage = round((v/sum_audi) * 100)
            print(f"    For {k} => {percentage}%" )
      
      if key == 'bmw':
         print(f"Sum_bmw: {sum_bmw}")
         for k, v in value.items():
            percentage = round((v/sum_bmw) * 100)
            print(f"    For {k} => {percentage}%" )
     

if __name__ == "__main__":
   main()