#Example for microsoft/Phi-3-mini-4k-instruct

docker network create my-network

docker run --gpus all --shm-size 1g -v D:/docker_volume:/data --name tgi-server --network my-network ghcr.io/huggingface/text-generation-inference:2.0.3 --model-id microsoft/Phi-3-mini-4k-instruct

docker build -t my_repository.com/my_first_container:latest .

docker run -p 15000:8501 --network my-network my_repository.com/my_first_container:latest