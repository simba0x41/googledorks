"""Tesla Google Scrapper

Usage:
  tesla.py <search> <pages> <processes>
  tesla.py (-h | --help)

Arguments:
  <search>        String to be Searched
  <pages>         Number of pages
  <processes>     Number of parallel processes

Options:
  -h, --help     Show this screen.

"""
from tesla import *
 
if __name__ == '__main__':
    arguments = docopt( __doc__, version='T3sla Google Scrapper' )
    search    = arguments['<search>']
    pages     = arguments['<pages>']
    processes   = int(arguments['<processes>'])
    start = timer()
    result = dorks(search,pages, processes)
    print ( *result, sep = '\n' )
    print( '\nTotal URLs Scraped : %s ' % str( len( result ) ) )
    print( 'Script Execution Time : %s ' % ( timer() - start, ) )
 
 
