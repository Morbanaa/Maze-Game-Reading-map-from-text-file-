from other import GameManager
import time

def main():
    game_manager = GameManager()
    game_manager.finish_map()

    counter = 0
    time_passed = 0
    while True:
        game_manager.update_game()
        game_manager.render_world(time_passed)

        time.sleep(.1)
        counter += 1
        if counter >= 10:
            counter = 0
            time_passed += 1
        


if __name__ == "__main__":
    main()
