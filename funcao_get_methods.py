# função para saber os métodos aplicáveis em um obj

def get_methods(object, tipo: str='pd', spacing=20):
  """Para saber os métodos aplicáveis no objeto.
     object->nome do objeto a se saber os métodos
     tipo->'df' é padrão, se não 'p' para print"""
  if tipo == 'pd':
    import pandas as pd

    methodList = []
    MethodDescription = []

    for method_name in dir(object):
      try:
          if callable(getattr(object, method_name)):
              methodList.append(str(method_name))
      except Exception:
          methodList.append(str(method_name))
    processFunc = (lambda s: ' '.join(s.split())) or (lambda s: s)
    
    for method in methodList:
      try:
          MethodDescription.append(str(method.ljust(spacing)) + ' ' +
                processFunc(str(getattr(object, method).__doc__)[0:90]))
      except Exception:
          MethodDescription.append(
                processFunc(str(getattr(object, method).__doc__)[0:100]))
    
    dicionario = {'metodo': methodList,
                'descricao': MethodDescription}
    metodos_df = pd.DataFrame(dicionario)

    return metodos_df
  
  elif tipo == 'p':
    methodList = []
  for method_name in dir(object):
    try:
        if callable(getattr(object, method_name)):
            methodList.append(str(method_name))
    except Exception:
        methodList.append(str(method_name))
  processFunc = (lambda s: ' '.join(s.split())) or (lambda s: s)
  for method in methodList:
    try:
        print(str(method.ljust(spacing)) + ' ' +
              processFunc(str(getattr(object, method).__doc__)[0:90]))
    except Exception:
        print(method.ljust(spacing) + ' ' + ' getattr() failed')