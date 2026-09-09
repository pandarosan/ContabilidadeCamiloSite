export async function onRequest(context) {
    try {
        const { env } = context;
        
        // Mock fallback para testes locais sem o KV bindado
        if (!env.ENQUETE_VOTOS_KV) {
            return new Response(JSON.stringify({ 
                opcao_a: 0, 
                opcao_b: 0, 
                total: 0 
            }), { 
                headers: { "Content-Type": "application/json" } 
            });
        }

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
