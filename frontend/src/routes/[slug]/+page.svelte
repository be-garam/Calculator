<script>
    import { fetchData } from '$lib/fetchData.js';
</script>

<div>
    {#await fetchData("api/sub", "POST", {a: 1, b: 3})}
    <b>Loading...</b>
    {:then data}
    <b>{data.result}</b>
    {/await}
</div>