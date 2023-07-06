source .venv/bin/activate

python Generation_scripts/Generate_Cubic.py
cd Processing_scripts
python Process_cubic.py
cd .. 
python data_visualization.py