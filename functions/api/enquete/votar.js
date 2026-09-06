export async function onRequestPost(context) {
    try {
        const { request, env } = context;
        const data = await request.json();
        const optionId = data.option;

        if (!['opcao_a', 'opcao_b', 'opcao_c'].includes(optionId)) {
            return new Response(JSON.stringify({ error: "Opção inválida" }), { status: 400 });
        }

        // Mock fallback para testes locais sem o KV bindado
        if (!env.ENQUETE_VOTOS_KV) {
            return new Response(JSON.stringify({ 
                opcao_a: optionId === 'opcao_a' ? 46 : 45, 
                opcao_b: optionId === 'opcao_b' ? 31 : 30, 
                opcao_c: optionId === 'opcao_c' ? 26 : 25, 
                total: 101 
            }), { 
                headers: { "Content-Type": "application/json" } 
            });
        }

        let current = parseInt(await env.ENQUETE_VOTOS_KV.get(optionId)) || 0;
        current += 1;
        await env.ENQUETE_VOTOS_KV.put(optionId, current.toString());

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
