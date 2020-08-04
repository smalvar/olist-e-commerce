def join_categories(df):
  df['product_category_name'] = df['product_category_name'].replace('telefonia_fixa', 'telefonia')\
  .replace('eletrodomesticos_2', 'eletrodomesticos'). replace('bebes', 'brinquedos_e_bebes')\
  .replace('fraldas_higiene', 'brinquedos_e_bebes').replace('brinquedos', 'brinquedos_e_bebes')\
  .replace('artes', 'artes_e_artesanato').replace('bebidas', 'alimentos_bebidas'). replace('alimentos', 'alimentos_bebidas')\
  .replace('casa_conforto_2', 'casa_conforto').replace('musica', 'musicas_cds_dvds_blu_ray')\
  .replace('cds_dvds_musicais', 'musicas_cds_dvds_blu_ray').replace('dvds_blu_ray', 'musicas_cds_dvds_blu_ray')\
  .replace('livros_importados', 'livros').replace('livros_tecnicos', 'livros').replace('livros_interesse_geral', 'livros')\
  .replace('fashion_bolsas_e_acessorios', 'moda_beleza_perfumaria').replace('fashion_calcados', 'moda_beleza_perfumaria')\
  .replace('fashion_underwear_e_moda_praia', 'moda_beleza_perfumaria')\
  .replace('fashion_roupa_masculina', 'moda_beleza_perfumaria').replace('fashion_roupa_feminina', 'moda_beleza_perfumaria')\
  .replace('fashion_esporte', 'moda_beleza_perfumaria').replace('fashion_roupa_infanto_juvenil', 'moda_beleza_perfumaria')\
  .replace('relogios_presentes', 'moda_beleza_perfumaria').replace('perfumaria', 'moda_beleza_perfumaria')\
  .replace('construcao_ferramentas_construcao', 'construção_ferramentas').replace('casa_construcao', 'construção_ferramentas')\
  .replace('construcao_ferramentas_seguranca', 'construção_ferramentas')\
  .replace('construcao_ferramentas_ferramentas', 'construção_ferramentas')\
  .replace('construcao_ferramentas_iluminacao', 'construção_ferramentas')\
  .replace('construcao_ferramentas_jardim', 'construção_ferramentas')\
  .replace('moveis_decoracao', 'moveis_decoracao')\
  .replace('moveis_escritorio', 'moveis_decoracao')\
  .replace('moveis_sala', 'moveis_decoracao')\
  .replace('moveis_cozinha_area_de_servico_jantar_e_jardim', 'moveis_decoracao')\
  .replace('moveis_quarto', 'moveis_decoracao')\
  .replace('moveis_colchao_e_estofado', 'moveis_decoracao')\
  .replace('informatica_acessorios', 'informatica_tablets')\
  .replace('pcs', 'informatica_tablets')\
  .replace('pc_gamer', 'informatica_tablets')\
  .replace('tablets_impressao_imagem', 'informatica_tablets')\
  .replace('agro_industria_e_comercio', 'industria_comercio')\
  .replace('industria_comercio_e_negocios', 'industria_comercio')\
  .replace('portateis_casa_forno_e_cafe', 'portateis_casa')\
  .replace('portateis_cozinha_e_preparadores_de_alimentos', 'portateis_casa')\
  .replace('artigos_de_festas', 'artigos_festas')\
  .replace('artigos_de_natal', 'artigos_festas')\
  .replace('eletronicos', 'eletronicos_games')\
  .replace('consoles_games', 'eletronicos_games')\
  .replace('eletronicos_games', 'eletronicos_games_livros')\
  .replace('livros', 'eletronicos_games_livros')\
  .replace('cine_foto', 'cine_foto_audio')\
  .replace('audio', 'cine_foto_audio')\
  .replace('sinalizacao_e_seguranca', 'sinalizacao_e_seguranca_servicos')\
  .replace('seguros_e_servicos', 'sinalizacao_e_seguranca_servicos')
  return df