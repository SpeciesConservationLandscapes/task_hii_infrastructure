#!/bin/bash

docker run -it -v $PWD/.config:/root/.config scl3/task_hii_infrastructure python hii_infrastructure.py -r 'Afrotropic' 
docker run -it -v $PWD/.config:/root/.config scl3/task_hii_infrastructure python hii_infrastructure.py -r 'Australasia' 
docker run -it -v $PWD/.config:/root/.config scl3/task_hii_infrastructure python hii_infrastructure.py -r 'Indomalayan' 
docker run -it -v $PWD/.config:/root/.config scl3/task_hii_infrastructure python hii_infrastructure.py -r 'Nearctic' 
docker run -it -v $PWD/.config:/root/.config scl3/task_hii_infrastructure python hii_infrastructure.py -r 'Neotropic' 
docker run -it -v $PWD/.config:/root/.config scl3/task_hii_infrastructure python hii_infrastructure.py -r 'Oceania' 
docker run -it -v $PWD/.config:/root/.config scl3/task_hii_infrastructure python hii_infrastructure.py -r 'Palearctic' 
docker run -it -v $PWD/.config:/root/.config scl3/task_hii_infrastructure python hii_infrastructure.py -r 'HighArctic' 
