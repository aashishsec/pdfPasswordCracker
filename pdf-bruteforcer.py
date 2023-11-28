import colorama,random,argparse,concurrent.futures
from PyPDF2 import PdfReader,PdfFileWriter
from os import path
from sys import exit
from termcolor import colored
from datetime import datetime

from colorama import Fore, Style

colorama.init(autoreset=True)

green = Fore.GREEN

magenta = Fore.MAGENTA

cyan = Fore.CYAN

mixed = Fore.RED + Fore.BLUE

red = Fore.RED

blue = Fore.BLUE

yellow = Fore.YELLOW

white = Fore.WHITE

reset = Style.RESET_ALL

colors = [magenta,cyan,mixed,red,blue,yellow, white]

random_color = random.choice(colors)

bold = Style.BRIGHT



def banner():

    print(f'''{bold}{random_color}

─────╔╗╔═╦═══╗────────────────────╔╦═══╗───────╔╗
─────║║║╔╣╔═╗║────────────────────║║╔═╗║───────║║
╔══╦═╝╠╝╚╣╚═╝╠══╦══╦══╦╗╔╗╔╦══╦═╦═╝║║─╚╬═╦══╦══╣║╔╦══╦═╗
║╔╗║╔╗╠╗╔╣╔══╣╔╗║══╣══╣╚╝╚╝║╔╗║╔╣╔╗║║─╔╣╔╣╔╗║╔═╣╚╝╣║═╣╔╝
║╚╝║╚╝║║║║║──║╔╗╠══╠══╠╗╔╗╔╣╚╝║║║╚╝║╚═╝║║║╔╗║╚═╣╔╗╣║═╣║
║╔═╩══╝╚╝╚╝──╚╝╚╩══╩══╝╚╝╚╝╚══╩╝╚══╩═══╩╝╚╝╚╩══╩╝╚╩══╩╝
║║
╚╝
        Author   : Aashish💕💕  
                                              
        Github   : https://github.com/aashish36
          
        pdfPasswordCracker is a Password Protected PDF file Bruteforcer with Python.

      ''')
    print("-" * 80)

    print(f"{bold}{random_color}pdfPasswordCracker starting at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

    print("-" * 80)

def get_args():
    
    parser=argparse.ArgumentParser(description=f"""{bold}{random_color}pdfPasswordCracker is a Password Protected PDF file Bruteforcer with Python.""")
   
    parser.add_argument('-w','--wordlist',metavar='wordlist',type=str,help=f"[{bold}{random_color}INFO]: {bold}{random_color}wordlist for passwords.")

    parser.add_argument('-p','--ProtectedPDF',metavar='ProtectedPDF',help=f"[{bold}{random_color}INFO]: {bold}{random_color}passwordProtectedPDF file.")
    
    return parser.parse_args()

def bruteforcepdf(pdfFile,wordlistfile):
    """Function to bruteforce pdf file"""
    passwords=[]
    with open(wordlistfile,'r') as f:
        f1=f.read().splitlines()
        for password in f1:
            passwords.append(password.strip())
            
    reader=PdfReader(pdfFile)
    for password in passwords:
        if str(reader.decrypt(password))=='PasswordType.OWNER_PASSWORD':
            print(colored(f"[+] Password Found : {password}",'green',attrs=['bold']))
            return password
            break


def decrypt_pdf(encypted_file,decrypted_file,password):
    with open(encypted_file,'rb') as encryptedFile, open(decrypted_file,'wb') as decrypteFile:
        reader=PdfReader(encryptedFile)
        if reader.is_encrypted:
            reader.decrypt(password)
        writer=PdfFileWriter()
        for i in range(reader.getNumPages()):
            writer.addPage(reader.getPage(i))
        writer.write(decrypted_file)
    print(colored(f"File Has been Succcessfully decrypted and saved at : {decrypted_file}",'cyan'))

def main():

    banner()

    args = get_args()

    pdfFile=args.ProtectedPDF

    if not path.exists(pdfFile):

        print(colored("[-] Please specify the location of Pdf file accurately ",'red'))

        exit(-1)

    
    wordlistfile=args.wordlist

    if not path.exists(wordlistfile):

        print(colored("[-] Please specify the location of wordlist file accurately ",'red'))

        exit(-1)


    password=bruteforcepdf(pdfFile,wordlistfile)

    if password:

        decrypt_pdf(pdfFile,f"decrypted-{path.basename(pdfFile)}",password)

    else:
        print(colored("[-] Password was not Found :",'red'))

if __name__=="__main__":

    main()