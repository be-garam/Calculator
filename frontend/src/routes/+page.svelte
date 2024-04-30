<script>
    import { Input, Label, Helper, Button, A, Card} from 'flowbite-svelte';
    import { fetchData } from '$lib/fetchData.js';
    import { goto } from '$app/navigation';

    let num1 = 0;
    let num2 = 0;

    async function handleClick(event, operation) {
        event.preventDefault();
        const result = await fetchData(`api/${operation}`, 'GET', { a: num1, b: num2 });
        // goto(`/result/+page.svelte?result=${result}`);
    }
</script>

<div class="container mx-auto flex items-center justify-center h-screen">
    <Card>
        <h1>Calculator</h1>
        <form>
            <div class="grid gap-6 mb-6 md:grid-cols-2">
                <div>
                    <Label for="num_1" class="mb-2">First num</Label>
                    <Input bind:value={num1} type="num" id="num_1" placeholder="1" required />
                </div>
                <div>
                    <Label for="num_2" class="mb-2">Second num</Label>
                    <Input bind:value={num2} type="num" id="num_2" placeholder="2" required />
                </div>
            </div>
            <div class="grid gap-6 mb-6 md:grid-cols-4">
                <Button on:click={(event) => { event.preventDefault(); handleClick(event, 'add');}} type="add" color="red"> + </Button>
                <Button on:click={(event) => { event.preventDefault(); handleClick(event, 'subtraction');}} type="subtraction" color="blue"> - </Button>
                <Button on:click={(event) => { event.preventDefault(); handleClick(event, 'multiplication');}} type="multiplication" color="yellow"> * </Button>
                <Button on:click={(event) => { event.preventDefault(); handleClick(event, 'division'); }} type="division" color="green"> / </Button>
            </div>
        </form>
    </Card>
</div>