# os movimentos artísticos são definidos por um conjunto de características, temas e estilos que os artistas seguem durante um período específico. Esses movimentos refletem as mudanças culturais, sociais e tecnológicas da época, influenciando a forma como a arte é criada e percebida. Abaixo estão alguns dos principais movimentos artísticos, cada um associado a palavras-chave que ajudam a identificar suas características distintas.

MOVEMENTS = {
    "Grega (beleza ideal e proporcao)": (
        'greek art OR "ancient greek" OR "classical greece" OR hellenic '
        'OR sculpture OR vase OR pottery OR statue OR relief OR mosaic OR painting'
    ),
    "Romana (realismo e monumentalidade)": (
        'roman art OR "ancient rome" OR "roman empire" OR sculpture OR bust '
        'OR relief OR fresco OR mosaic OR architecture'
    ),
    "Paleocrista": (
        '"early christian" OR paleochristian OR catacomb OR basilica OR mosaic '
        'OR fresco OR icon OR church'
    ),
    "Bizantina (mosaicos e arte religiosa)": (
        'byzantine OR "byzantine art" OR mosaic OR icon OR church OR religious'
    ),
    "Romanica (formas solidas e temas biblicos)": (
        'romanesque OR "romanesque art" OR church OR cathedral OR fresco '
        'OR sculpture OR tympanum'
    ),
    "Gotica (vitrais, verticalidade e luz)": (
        'gothic OR "gothic art" OR "stained glass" OR cathedral OR altarpiece '
        'OR illumination OR sculpture'
    ),
    "Renascimento (XIV-XVI)": (
        'renaissance OR "italian renaissance" OR Leonardo OR Michelangelo '
        'OR Raphael OR painting OR fresco OR sculpture'
    ),
    "Maneirismo (XVI)": (
        'mannerism OR manierismo OR "El Greco" OR Parmigianino OR Pontormo '
        'OR Bronzino OR painting OR altarpiece'
    ),
    "Barroco (XVII-XVIII)": (
        'baroque OR barroco OR Caravaggio OR Rubens OR Rembrandt OR Bernini '
        'OR Velazquez OR painting OR sculpture'
    ),
    "Rococo (XVIII)": (
        'rococo OR rococó OR Watteau OR Fragonard OR Boucher OR painting OR portrait'
    ),
    "Neoclassicismo (XVIII-XIX)": (
        'neoclassicism OR neoclassical OR "Jacques-Louis David" OR Ingres '
        'OR Canova OR painting OR sculpture'
    ),
    "Romantismo (XIX)": (
        'romanticism OR romantismo OR Delacroix OR Goya OR Turner OR Friedrich OR painting'
    ),
    "Realismo (XIX)": (
        'realism art OR realismo OR Courbet OR Millet OR Daumier OR painting'
    ),
    "Impressionismo (XIX)": (
        'impressionism OR impressionist OR Monet OR Renoir OR Degas OR Pissarro OR painting'
    ),
    "Pos-Impressionismo (XIX)": (
        '"post-impressionism" OR postimpressionism OR "Van Gogh" OR Cezanne '
        'OR Gauguin OR Seurat OR painting'
    ),
    "Expressionismo (XX)": (
        'expressionism OR expressionist OR Munch OR Kirchner OR Kandinsky OR painting'
    ),
    "Cubismo (XX)": (
        'cubism OR cubist OR Picasso OR Braque OR Gris OR painting'
    ),
    "Futurismo (XX)": (
        'futurism OR futurist OR Boccioni OR Balla OR Severini OR painting OR sculpture'
    ),
    "Dadaismo (XX)": (
        'dada OR dadaism OR Duchamp OR Arp OR Hausmann OR artwork OR collage OR painting'
    ),
    "Surrealismo (XX)": (
        'surrealism OR surrealist OR Dali OR Magritte OR Ernst OR Miro OR painting'
    ),
}