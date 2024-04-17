<script>
  import "../app.pcss";
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
</script>

<div class="w-screen h-screen">
    <Navbar>
      <NavBrand href="/">
        <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Logo</span>
      </NavBrand>
    <NavHamburger />
    <NavUl>
      <NavLi href="/">Home</NavLi>
      <NavLi href="/about">About</NavLi>
    </NavUl>
  </Navbar>
  <div class="container mx-auto h-full">
    <div class="container mx-auto my-auto h-full">
      <slot></slot>
    </div>
  </div>
</div>
