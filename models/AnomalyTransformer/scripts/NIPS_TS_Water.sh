export CUDA_VISIBLE_DEVICES=2

python main.py --anormly_ratio 1 --num_epochs 3   --batch_size 256  --mode train --dataset NIPS_TS_Water  --data_path dataset/NIPS_TS_Water  --input_c 9 --output_c 9 
python main.py --anormly_ratio 1  --num_epochs 10     --batch_size 256   --mode test    --dataset NIPS_TS_Water   --data_path dataset/NIPS_TS_Water --input_c 9    --output_c 9


