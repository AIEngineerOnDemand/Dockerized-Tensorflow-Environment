import tensorflow as tf

# Some example data
x_data = tf.random.normal(shape=[100])
y_data = x_data * 3 + 2 + tf.random.normal(shape=[100])

# Initialize the slope and y-intercept as trainable variables
m = tf.Variable(0.0, trainable=True)
b = tf.Variable(0.0, trainable=True)

# Define the linear function
def linear_function(x):
    return m * x + b

# Define the loss function (mean squared error)
def loss_function(y_true, y_pred):
    return tf.reduce_mean(tf.square(y_true - y_pred))

# Define the optimizer (stochastic gradient descent)
optimizer = tf.optimizers.SGD(learning_rate=0.01)

# Training loop
for _ in range(1000):
    # Use tf.GradientTape to record the operations
    with tf.GradientTape() as tape:
        y_pred = linear_function(x_data)
        loss = loss_function(y_data, y_pred)

    # Compute the gradients of the loss with respect to m and b
    gradients = tape.gradient(loss, [m, b])

    # Update m and b to minimize the loss
    optimizer.apply_gradients(zip(gradients, [m, b]))

print(f"Final values: m = {m.numpy()}, b = {b.numpy()}")