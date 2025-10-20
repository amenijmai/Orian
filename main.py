import argparse
from agent import OrionAgent
import time

def main(mode='preview'):
    agent = OrionAgent()
    if mode == 'preview':
        actions = agent.run_once()
        print('Preview actions:')
        for a in actions:
            print('-', a)
    elif mode == 'loop':
        try:
            while True:
                actions = agent.run_once()
                if actions:
                    print('Actions:', actions)
                time.sleep(30)  # poll every 30s
        except KeyboardInterrupt:
            print('Stopped')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['preview', 'loop'], default='preview')
    args = parser.parse_args()
    main(args.mode)
