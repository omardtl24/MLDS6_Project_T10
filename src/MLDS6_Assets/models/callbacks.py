from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau

def create_callbacks(model_name):
    """
    Crea una lista de callbacks para monitorizar y optimizar el entrenamiento.

    Args:
        model_name (str): Nombre del modelo para guardar los checkpoints.

    Returns:
        list: Lista de callbacks.
    """
    checkpoint = ModelCheckpoint(
        f'best_{model_name}.keras',
        monitor='val_accuracy',
        mode='max',
        save_best_only=True,
        verbose=1
    )

    early_stopping = EarlyStopping(
        monitor='val_loss',
        patience=10,
        restore_best_weights=True,
        verbose=1
    )

    reduce_lr = ReduceLROnPlateau(
        monitor='val_loss',
        factor=0.2,
        patience=5,
        min_lr=1e-6,
        verbose=1
    )

    return [checkpoint, early_stopping, reduce_lr]
