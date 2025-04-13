# Now that you have a feeling for working with strings, we are going to make things a bit more difficult

# Your task is to the the input() function to play a game using gymnasium

# Step 1: import gymnasium 
import gymnasium as gym
import ale_py


# Step 2: write the function 'text_to_action()'
def text_to_action(s: str):
    # hint: parse the text (use the same idea as before)

    # make sure that the text chooses a correct action:
    # see: https://ale.farama.org/environments/pong/

    # map the action choice to a number

    # return the number
    pass


if __name__ == '__main__':
    gym.register_envs(ale_py)
    env = gym.make("ALE/Pong-v5")
    
    # Reset the environment to generate the first observation
    observation, info = env.reset(seed=42)
    for _ in range(1000):
        # step 3: read text using input()
        text = ...
        # step 4: parse the text
        action = ...

        # step (transition) through the environment with the action
        # receiving the next observation, reward and if the episode has terminated or truncated
        observation, reward, terminated, truncated, info = env.step(action)

        # If the episode has ended then we can reset to start a new episode
        if terminated or truncated:
            observation, info = env.reset()

    env.close()