import matplotlib.pyplot as plt # type: ignore
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau # type: ignore
import time

def createCallbacks(model_name):
    """
    Generates a list of callbacks for model training, including:
    - ModelCheckpoint: Saves the best model based on validation accuracy.
    - EarlyStopping: Stops training if validation loss doesn't improve.
    - ReduceLROnPlateau: Reduces learning rate when validation loss stagnates.

    Parameters:
    - model_name (str): Name used to save the best model.

    Returns:
    - list: A list of Keras callbacks (ModelCheckpoint, EarlyStopping, ReduceLROnPlateau).
    """

    # Checkpoint para guardar el mejor modelo
    checkpoint = ModelCheckpoint(
        f'best_{model_name}.keras',  
        monitor='val_accuracy',      
        mode='max',                  
        save_best_only=True,         
        verbose=1                    
    )

    # Early stopping para prevenir overfitting
    early_stopping = EarlyStopping(
        monitor='val_loss',         
        patience=3,                 
        restore_best_weights=True,  
        verbose=1                   
    )

    # Reducción de learning rate cuando el entrenamiento se estanca
    reduce_lr = ReduceLROnPlateau(
        monitor='val_loss',          
        factor=0.2,                  
        patience=3,                  
        min_lr=1e-6,                
        verbose=1                    
    )

    return [checkpoint, early_stopping, reduce_lr]


def trainModel(model, model_name, train_data, validation_data, epochs=10, callbacks=None):
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
    callbacks = createCallbacks(model_name)
    start = time.time()
    history = model.fit(
        train_data,
        epochs=epochs,
        validation_data=validation_data,
        callbacks=callbacks,
        verbose=1
    )
    end = time.time()
    t = end-start
    hours = t // 3600
    minutes = (t % 3600) // 60
    seconds = t % 60
    print(f'{model_name} training time for {epochs} epochs was: {hours}h {minutes}m {seconds}s')
    return history

def plotTrainingHistory(history, model_name):
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
