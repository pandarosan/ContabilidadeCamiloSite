with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = """
/* ========================================================= */
/* ALERTS / ZONA DE AVISOS */
/* ========================================================= */
.alert-msg {
    animation: slideDownFade 0.4s ease-out forwards;
}

@keyframes slideDownFade {
    0% {
        opacity: 0;
        transform: translateY(-10px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

/* ========================================================= */
/* IMPRESSÃO (RELATÓRIO COMERCIAL) */
/* ========================================================= */
@media print {
    /* Ocultar elementos desnecessários na impressão */
    header, footer, nav, .seo-content, .calc-header-global, .btn-wrapper, #cta-resultado, .contato-header {
        display: none !important;
    }

    /* Mostrar cabeçalho e rodapé exclusivos de impressão */
    .print-header {
        display: block !important;
    }
    #print-footer {
        display: block !important;
    }

    /* Ajustar fundo e bordas para economizar tinta e focar no conteúdo */
    body {
        background-color: white !important;
        color: black !important;
    }
    main {
        background-color: white !important;
        padding-top: 0 !important;
    }
    .calc-layout-wrapper {
        margin: 0 !important;
        padding: 0 !important;
        display: block !important;
    }
    .calc-container-wrapper {
        width: 100% !important;
        margin: 0 !important;
    }
    .calc-container {
        box-shadow: none !important;
        padding: 0 !important;
        border: none !important;
    }

    /* Forçar cores do cabeçalho da tabela */
    .calc-table th {
        color: black !important;
        border-bottom: 2px solid black !important;
    }
    
    /* Garantir que as linhas sejam visíveis */
    .calc-table tr {
        border-bottom: 1px solid #ccc !important;
    }
    
    /* Remover bordas dos inputs para parecer texto normal */
    .form-control {
        border: none !important;
        background: transparent !important;
        box-shadow: none !important;
        color: black !important;
    }
}
"""

if "/* IMPRESSÃO" not in css:
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write("\n" + new_css)
    print("CSS updated.")
else:
    print("CSS already contains print styles.")
