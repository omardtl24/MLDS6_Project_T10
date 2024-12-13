import matplotlib.pyplot as plt

def train_model(model, model_name, train_data, validation_data, epochs=10, callbacks=None):
    """
    Entrena un modelo con los datos de entrenamiento y validación.

    Args:
        model (keras.Model): Modelo a entrenar.
        model_name (str): Nombre del modelo.
        train_data: Datos de entrenamiento.
        validation_data: Datos de validación.
        epochs (int): Número de épocas.
        callbacks (list): Lista de callbacks.

    Returns:
        keras.callbacks.History: Historia del entrenamiento.
    """
    history = model.fit(
        train_data,
        epochs=epochs,
        validation_data=validation_data,
        callbacks=callbacks,
        verbose=1
    )
    return history

def plot_training_history(history, model_name):
    """
    Genera gráficos de precisión y pérdida a lo largo del entrenamiento.

    Args:
        history (keras.callbacks.History): Historia del entrenamiento.
        model_name (str): Nombre del modelo.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

    ax1.plot(history.history['accuracy'], label='train')
    ax1.plot(history.history['val_accuracy'], label='validation')
    ax1.set_title(f'{model_name} - Accuracy')
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Accuracy')
    ax1.legend()

    ax2.plot(history.history['loss'], label='train')
    ax2.plot(history.history['val_loss'], label='validation')
    ax2.set_title(f'{model_name} - Loss')
    ax2.set_xlabel('Epoch')
    ax2.set_ylabel('Loss')
    ax2.legend()

    plt.tight_layout()
    plt.show()
