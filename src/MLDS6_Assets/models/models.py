import tensorflow as tf
from tensorflow.keras import layers, models

def configModelV1(baseModel, lr=1e-3):
    """
    Configura un modelo con dos capas densas y regularización.

    Args:
        baseModel (keras.Model): Modelo base preentrenado.
        lr (float): Learning rate.

    Returns:
        keras.Model: Modelo completo.
    """
    input = layers.Input(shape=(765, 500, 3))
    x = baseModel(input)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dense(512, activation='relu')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(0.5)(x)
    x = layers.Dense(256, activation='relu')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(0.3)(x)
    output = layers.Dense(3, activation='softmax')(x)

    complete_model = models.Model(inputs=input, outputs=output)
    complete_model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=lr),
        loss='categorical_crossentropy',
        metrics=[
            'accuracy',
            tf.keras.metrics.TopKCategoricalAccuracy(k=2, name='top_2_accuracy'),
            tf.keras.metrics.AUC(multi_label=True)
        ]
    )
    return complete_model

def configModelV2(baseModel, lr=1e-3):
    """
    Configura un modelo con tres capas densas y regularización.

    Args:
        baseModel (keras.Model): Modelo base preentrenado.
        lr (float): Learning rate.

    Returns:
        keras.Model: Modelo completo.
    """
    input = layers.Input(shape=(765, 500, 3))
    x = baseModel(input)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dense(128, activation='relu')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(0.5)(x)
    x = layers.Dense(64, activation='relu')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(0.3)(x)
    x = layers.Dense(32, activation='relu')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(0.2)(x)
    output = layers.Dense(3, activation='softmax')(x)

    complete_model = models.Model(inputs=input, outputs=output)
    complete_model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=lr),
        loss='categorical_crossentropy',
        metrics=[
            'accuracy',
            tf.keras.metrics.TopKCategoricalAccuracy(k=2, name='top_2_accuracy'),
            tf.keras.metrics.AUC(multi_label=True)
        ]
    )
    return complete_model
