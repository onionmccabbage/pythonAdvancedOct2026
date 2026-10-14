import pstats # this lets us read the output of cProfile

def main():
    '''read and display profile output'''
    p = pstats.Stats('prof_out')
    p.print_stats()

if __name__ == '__main__':
    main()