run:
	uv run super_mario.py

clean:
	rm -rf __pycache__

install:
	uv pip install pygame
