<script>
    import { Input, Label, Helper, Button, A, Card} from 'flowbite-svelte';
</script>
  
<div class="container mx-auto flex items-center justify-center h-screen">
    <Card>
        <h1>Calculator</h1>
        <form>
            <div class="grid gap-6 mb-6 md:grid-cols-2">
                <div>
                    <Label for="num_1" class="mb-2">First num</Label>
                    <Input type="num" id="num_1" placeholder="1" required />
                </div>
                <div>
                    <Label for="num_2" class="mb-2">Second num</Label>
                    <Input type="num" id="num_2" placeholder="2" required />
                </div>
            </div>
            <div class="grid gap-6 mb-6 md:grid-cols-4">
                <Button type="add" color="red"> + </Button>
                <Button type="subtraction" color="blue"> - </Button>
                <Button type="multiplication" color="yellow"> * </Button>
                <Button type="division" color="green"> / </Button>
            </div>
        </form>
    </Card>
</div>