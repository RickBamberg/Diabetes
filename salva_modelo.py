import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import RobustScaler, StandardScaler

# 1. Carregar seus dados originais
try:
    df = pd.read_csv('date/diabetesX.csv')  # Ajuste o nome/caminho do arquivo
    print("Colunas disponíveis no arquivo:", df.columns.tolist())
    
    # Verificar se a coluna target existe
    target_column = 'Resultado'  # Altere para o nome correto da sua coluna target
    if target_column not in df.columns:
        raise ValueError(f"Coluna target '{target_column}' não encontrada. Colunas disponíveis: {df.columns.tolist()}")
    
    X_train = df.drop(target_column, axis=1)  # Features
    y_train = df[target_column]              # Target

    # 2. Definir o pré-processador (ajuste conforme suas colunas reais)
    numeric_features = ['Insulina', 'Espessura da pele', 'IMC', 'Glicose', 'Pressão arterial']
    pass_features = ['Gravidez', 'Idade', 'Diabetes Descendente']
    
    # Verificar se todas as colunas existem
    missing_cols = [col for col in numeric_features + pass_features if col not in X_train.columns]
    if missing_cols:
        raise ValueError(f"Colunas não encontradas: {missing_cols}. Colunas disponíveis: {X_train.columns.tolist()}")

    preprocessor = ColumnTransformer(
        transformers=[
            ('robust', RobustScaler(), ['Insulina', 'Espessura da pele', 'IMC']),
            ('standard', StandardScaler(), ['Glicose', 'Pressão arterial']),
            ('pass', 'passthrough', pass_features)
        ],
        remainder='passthrough'
    )

    # 3. Treinar o pipeline
    print("Pré-processando os dados...")
    X_train_processed = preprocessor.fit_transform(X_train)

    print("Treinando o modelo...")
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        random_state=42
    )
    model.fit(X_train_processed, y_train)

    # 4. Salvar os artefatos
    print("Salvando os arquivos...")
    joblib.dump(preprocessor, 'model/preprocessor.pkl')
    joblib.dump(model, 'model/model.pkl')

    print("✅ Modelo e pré-processador salvos com sucesso!")
    print("Arquivos gerados:")
    print("- preprocessor.pkl")
    print("- model.pkl")

except Exception as e:
    print(f"❌ Ocorreu um erro: {str(e)}")
    print("Verifique:")
    print("- O nome/caminho do arquivo CSV está correto?")
    print("- O nome da coluna target está correto?")
    print("- Todas as colunas mencionadas no pré-processador existem no arquivo?")
