import click
# pip install -U click

@click.command()
@click.option('--count', type = int, default = 2, help = 'number of greetings~')
#python main.py --count 3
#python main.py --help
@click.argument('name', default = 'sang')
#python main.py sang



def hello(count,name):
    '''
    help message
    '''
    for x in range(count):
        print(f"hello {name}")
    
if __name__== "__main__":
    hello()
    
    
# 시