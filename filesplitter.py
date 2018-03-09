import os, argparse

def getArgsDict():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--chunksize", default='512', help="chunk size in byte")
    parser.add_argument("-p", "--pause", action="store_true", help="pause")
    parser.add_argument("-t", "--to", default="to", help="to file")
    parser.add_argument("-f", "--from", default="from", help="from file")
    
    return parser.parse_args()

def main():
    args = getArgsDict()
    chunksize = int(args.chunksize)
    inputDir = './'
    outFilePath = os.path.join(inputDir, 'out.ts')
    inFilePath = os.path.join(inputDir, 'maybe.ts')
    with open(inFilePath, 'rb') as inFile:
        data = inFile.read(chunksize)
        while data:
            with open(outFilePath, 'ab') as outFile:
                outFile.write(data)
            if args.pause:
                input('press to read next chunk')
            data = inFile.read(chunksize)

if __name__=='__main__':
    main() # D:\>python filesplitter.py --to to.ts --from from.ts --chunksize 200000000 -p
