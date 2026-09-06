export async function onRequest(context) {
    try {
        const { env } = context;
        
        // Mock fallback para testes locais sem o KV bindado
        if (!env.ENQUETE_VOTOS_KV) {
            return new Response(JSON.stringify({ 
                opcao_a: 45, 
                opcao_b: 30, 
                opcao_c: 25, 
                total: 100 
            }), { 
                headers: { "Content-Type": "application/json" } 
            });
        }

        const opcaoA = parseInt(await env.ENQUETE_VOTOS_KV.get('opcao_a')) || 0;
        const opcaoB = parseInt(await env.ENQUETE_VOTOS_KV.get('opcao_b')) || 0;
        const opcaoC = parseInt(await env.ENQUETE_VOTOS_KV.get('opcao_c')) || 0;
        const total = opcaoA + opcaoB + opcaoC;

        return new Response(JSON.stringify({
            opcao_a: opcaoA,
            opcao_b: opcaoB,
            opcao_c: opcaoC,
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
