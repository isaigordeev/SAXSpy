source .venv/bin/activate

python Generation_scripts/Generate_Cubic.py -phase "cubic" --mph "Pn3m"
cd Processing_scripts
python Process_cubic.py
cd .. 
python main.py -phase "cubic" --mph "Pn3m"