import os
import sys
import json
import argparse
import pandas as pd


def process_directory(dirpath):
    filepath = os.path.join(dirpath, 'metadata.json')
    with open(filepath, 'r') as file:
        metadata = json.load(file)
    return metadata


def process_all_directories(root_dir):
    all_metadata = []
    for dirname in os.listdir(root_dir):
        dirpath = os.path.join(root_dir, dirname)
        if os.path.isdir(dirpath):
            metadata = process_directory(dirpath)
            metadata['dirpath'] = dirpath
            all_metadata.append(metadata)
    return all_metadata


def generate_csv(metadata, filepath):
    df = pd.DataFrame(data=metadata)
    df.to_csv(filepath, index=False, header=True)


def parse_args():
    '''
    '''
    parser = argparse.ArgumentParser()

    # the root directory containing the directories to process
    parser.add_argument('root_dir')

    # where to save the CSV of aggregated metadata
    parser.add_argument('--output-filepath', dest='output_filepath')

    args = parser.parse_args()
    return args


def main():
    '''
    '''
    args = parse_args()

    # concatenate the metadata 
    all_metadata = process_all_directories(args.root_dir)

    # save to a CSV if an output filepath was provided
    if args.output_filepath:
        print('Saving aggregated metadata to %s' % args.output_filepath)
        generate_csv(all_metadata, args.output_filepath)
    else:
        print(all_metadata)


if __name__ == '__main__':
    main()
