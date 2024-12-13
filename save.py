import gym

# Criando o ambiente com renderização explícita
env = gym.make("CartPole-v1", render_mode="human")

n_episodes = 10  # Número de episódios que o agente jogará
max_steps = 200  # Número máximo de passos por episódio

for episode in range(n_episodes):
    state, _ = env.reset()
    total_reward = 0

    for step in range(max_steps):
        env.render()
        action = env.action_space.sample()

        # Ajuste para garantir compatibilidade com np.bool8
        step_result = env.step(action)
        next_state, reward = step_result[0], step_result[1]
        done = bool(step_result[2])  # Converte 'done' para booleano padrão
        truncated = bool(step_result[3])  # Converte 'truncated' para booleano padrão
        total_reward += reward

        if done or truncated:
            print(f"Episódio {episode + 1} terminou após {step + 1} passos com recompensa total {total_reward}.")
            break

env.close()