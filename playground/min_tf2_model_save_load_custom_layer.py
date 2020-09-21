import tensorflow as tf
import numpy as np
import setGPU

print('tensorflow version: ', tf.__version__)

class CustomLayer(tf.keras.layers.Layer):
	def __init__(self, mean_x, var_x, **kwargs):
		super(CustomLayer, self).__init__(**kwargs)
		self.mean_x = mean_x
		self.var_x = var_x

	def call(self, x):
		return (x - self.mean_x) / self.var_x

	def get_config(self):
		config = super(CustomLayer, self).get_config()
		config.update({'mean_x': self.mean_x, 'var_x': self.var_x})
		return config



def make_model():
	inputs = tf.keras.Input(shape=(3,))
	x = tf.keras.layers.Dense(5)(inputs)
	x = CustomLayer(2., 1.)(x)
	outputs = tf.keras.layers.Softmax()(x)
	return tf.keras.Model(inputs, outputs)

model = make_model()
model.save('tmp_model.h5')
loaded_model = tf.keras.models.load_model('tmp_model.h5', custom_objects={'CustomLayer': CustomLayer})
x = tf.random.uniform((10, 3))
assert np.allclose(model.predict(x), loaded_model.predict(x))

