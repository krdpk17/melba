import numpy
import argparse

def get_randoms(dimension):
  table = numpy.random.random(dimension)
  return table

def main():
  parse=argparse.ArgumentParser(description='table with random values')
  parse.add_argument('integers',metavar='dimension',type=int, nargs='+',help='integers for the dimension')
  args = parse.parse_args()
  mytable = get_randoms(args.integers)
  print(mytable)

if __name__ == "__main__":
  main()
