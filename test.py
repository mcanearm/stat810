import jax
import time

# Define and JIT-compile the function
@jax.jit
def generate_randoms(key):
    return jax.random.normal(key, shape=(10**8,))

key = jax.random.PRNGKey(0)

# Measure JIT compilation (first call includes compilation)
new_key, sub_key = jax.random.split(key)
start_compile = time.time()
x = generate_randoms(sub_key)
x.block_until_ready()  # Ensure computation completes
end_compile = time.time()
compilation_time = end_compile - start_compile

# Measure “run” time (subsequent call uses cached compiled function)
new_key, sub_key2 = jax.random.split(new_key)
start_run = time.time()
x2 = generate_randoms(sub_key2)
x2.block_until_ready()
end_run = time.time()
run_time = end_run - start_run

print(f"First run time: {compilation_time:.4f} seconds")
print(f"Second run time: {run_time:.4f} seconds")

