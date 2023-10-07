import argparse
import warnings
warnings.filterwarnings('ignore')
import subprocess
import os
import csv


def print_output(proc):
    for line in iter(proc.stdout.readline, b''):
        print(line.decode('utf-8'), end='')


parser = argparse.ArgumentParser()

# Add all the parameters you need there
parser.add_argument('--model', metavar='-m', type=str, required=False, default='DCDetector',help='model name')
parser.add_argument('--dataset', metavar='-d', type=str, required=False, default='MSL', help='dataset name')
parser.add_argument('--instance', metavar='-i', type=str, required=False, default='15', help='instance number')

# only for Anomaly-transformer and DCdetector
parser.add_argument('--num_epochs', type=int, default=3)
parser.add_argument('--batch_size', type=int, default=128)
parser.add_argument('--input_c', type=int, default=55)
parser.add_argument('--output_c', type=int, default=55) 
parser.add_argument('--anormly_ratio', type=float, default=1.0)
parser.add_argument('--result_save_path', type=str, default='result/result.csv')

# other models' parameters
parser.add_argument('--rtdw_datafolder', type=str, default='../../datasets/rtdw/fillzero_std',help='holo_datafolder')
parser.add_argument('--public_datafolder', type=str, default='../../datasets/public/',help='public_datafolder')
parser.add_argument('--holo_result_save_path', type=str, default='../../result/holo_result.csv',help='holo_result_save_path')
parser.add_argument('--public_result_save_path', type=str, default='../../result/public_result.csv',help='public_result_save_path')

config = parser.parse_args()
args = vars(config)

config_command = f' --holo_result_save_path ../{config.holo_result_save_path} --public_result_save_path ../{config.public_result_save_path}'
config_command += f' --public_datafolder {config.public_datafolder} --holo_datafolder {config.holo_datafolder}'
config_command += f' --dataset {config.dataset} --instance {config.instance}'

if config.model == 'DCDetector':
    command =  "python main.py" + " --anormly_ratio " + str(config.anormly_ratio) + " --num_epochs " + str(config.num_epochs) + " --dataset " + config.dataset + " --batch_size " + str(config.batch_size)  + " --mode train " + " --data_path " + config.dataset + " --input_c " + str(config.input_c)  + " --output_c " + str(config.output_c) + " --result_save_path " + config.result_save_path + " --instance " + str(config.instance)
    command2 = "python main.py" + " --anormly_ratio " + str(config.anormly_ratio) + " --num_epochs " + str(config.num_epochs) + " --dataset " + config.dataset + " --batch_size " + str(config.batch_size)  + " --mode test " +  " --data_path " + config.dataset + " --input_c " + str(config.input_c)  + " --output_c " + str(config.output_c) + " --result_save_path " + config.result_save_path + " --instance " + str(config.instance)
elif config.model == 'AnomalyTransformer':
    command =  "python main.py" + " --anormly_ratio " + str(config.anormly_ratio) + " --num_epochs " + str(config.num_epochs) + " --dataset " + config.dataset + " --batch_size " + str(config.batch_size)  + " --mode train " + " --data_path " + config.dataset + " --input_c " + str(config.input_c)  + " --output_c " + str(config.output_c) + " --result_save_path " + config.result_save_path + " --instance " + str(config.instance)
    command2 = "python main.py" + " --anormly_ratio " + str(config.anormly_ratio) + " --num_epochs " + str(config.num_epochs) + " --dataset " + config.dataset + " --batch_size " + str(config.batch_size)  + " --mode test " +  " --data_path " + config.dataset + " --input_c " + str(config.input_c)  + " --output_c " + str(config.output_c) + " --result_save_path " + config.result_save_path + " --instance " + str(config.instance)
elif config.model == 'ECOD':
    command = "python ../models/classic/main.py --model ECOD" + config_command
elif config.model == 'USAD':
    command = "python ../models/usad/main.py" + config_command
elif config.model == 'COPOD':
    command = "python ../models/classic/main.py --model COPOD" + config_command
elif config.model == 'BeatGAN':
    command = "python ../models/BeatGAN/main.py" + config_command
elif config.model == 'LSTM-VAE':
    command = "python ../models/classic/main.py --model LSTM-VAE" + config_command
elif config.model == 'DAGMM':
    command = "python ../models/DAGMM/main.py " + config_command
elif config.model == 'DeepSVDD':
    command = "python ../models/classic/main.py --model DeepSVDD" + config_command
elif config.model == 'LSTM-AE':
    command = "python ../models/classic/main.py --model LSTM-AE" + config_command
elif config.model == 'LSTM':
    command = "python ../models/classic/main.py --model LSTM" + config_command
elif config.model == 'IForest':
    command = "python ../models/classic/main.py --model IForest" + config_command
elif config.model == 'KNN':
    command = "python ../models/classic/main.py --model KNN" + config_command
elif config.model == 'LOF':
    command = "python ../models/classic/main.py --model LOF" + config_command


proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print_output(proc)

if config.model == 'DCDetector' or config.model == 'AnomalyTransformer':
    proc2 = subprocess.Popen(command2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print_output(proc2)


