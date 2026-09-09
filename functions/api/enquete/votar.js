export async function onRequestPost(context) {
    try {
        const { request, env } = context;
        const data = await request.json();
        const optionId = data.option;

        if (!['opcao_a', 'opcao_b'].includes(optionId)) {
            return new Response(JSON.stringify({ error: "Opção inválida" }), { status: 400 });
        }

        // Mock fallback para testes locais sem o KV bindado
        if (!env.ENQUETE_VOTOS_KV) {
            return new Response(JSON.stringify({ 
                opcao_a: optionId === 'opcao_a' ? 1 : 0, 
                opcao_b: optionId === 'opcao_b' ? 1 : 0, 
                total: 1 
            }), { 
                headers: { "Content-Type": "application/json" } 
            });
        }

        let current = parseInt(await env.ENQUETE_VOTOS_KV.get(optionId)) || 0;
        current += 1;
        await env.ENQUETE_VOTOS_KV.put(optionId, current.toString());

        const opcaoA = parseInt(await env.ENQUETE_VOTOS_KV.get('opcao_a')) || 0;
        const opcaoB = parseInt(await env.ENQUETE_VOTOS_KV.get('opcao_b')) || 0;
        const total = opcaoA + opcaoB;

        return new Response(JSON.stringify({
            opcao_a: opcaoA,
            opcao_b: opcaoB,
            total: total
        }), {
            headers: {
                "Content-Type": "application/json"
            }
        });
    } catch (error) {
        return new Response(JSON.stringify({ error: error.message }), { status: 500 });
    }
}
