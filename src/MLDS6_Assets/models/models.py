from tensorflow.keras import layers, models, metrics, optimizers
def configModelV1(baseModel,hp, lr=1e-3):
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
    x = layers.Dense(hp.Choice('units', [128,256]), activation='relu')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(0.5)(x)
    x = layers.Dense(hp.Choice('units', [64,128]), activation='relu')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(0.3)(x) 
    output = layers.Dense(3, activation='softmax')(x)

    complete_model = models.Model(inputs=input, outputs=output)
    complete_model.compile(
        optimizer=optimizers.Adam(learning_rate=lr),
        loss='categorical_crossentropy',
        metrics=[
            'accuracy',
            metrics.TopKCategoricalAccuracy(k=2, name='top_2_accuracy'),
            metrics.AUC(multi_label=True)
        ]
    )
    return complete_model

def configModelV2(baseModel,hp, lr=1e-3):
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
    x = layers.Dense(hp.Choice('units', [32,64,128]), activation='relu')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(0.5)(x)
    x = layers.Dense(hp.Choice('units', [16,32,64]), activation='relu')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(0.3)(x)
    x = layers.Dense(hp.Choice('units', [8,16,32]), activation='relu')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(0.2)(x)
    output = layers.Dense(3, activation='softmax')(x)

    complete_model = models.Model(inputs=input, outputs=output)
    complete_model.compile(
        optimizer=optimizers.Adam(learning_rate=lr),
        loss='categorical_crossentropy',
        metrics=[
            'accuracy',
            metrics.TopKCategoricalAccuracy(k=2, name='top_2_accuracy'),
            metrics.AUC(multi_label=True)
        ]
    )
    return complete_model
