const cart = document.getElementById("cart");
const openBtn = document.getElementById("cart-button");
const closeBtn = document.getElementById("close-cart");

let total = 0;

openBtn.addEventListener("click", () => {
  cart.classList.add("active");
});

closeBtn.addEventListener("click", () => {
  cart.classList.remove("active");
});

function addToCart(nome, preco) {
  const cartItems = document.getElementById("cart-items");
  const cartTotal = document.getElementById("cart-total");

  const item = document.createElement("div");
  item.innerHTML = `<p>${nome} - R$ ${preco}</p>`;

  cartItems.appendChild(item);

  total += preco;
  cartTotal.innerText = total.toFixed(2);

  cart.classList.add("active");
}


async function mostrar_carrinho() {
  const resposta = await fetch("http://10.110.134.2:8080/api/get/carrinho");

  if (!resposta.ok) {
    alert("Erro ao obter o carrinho:");
  } else {
    const dadosCarrinho = await resposta.json()
    const carrinho = document.querySelector("#cart-items");

    carrinho.innerHTML = "";

    let total = 0;

    for (let item of dadosCarrinho) {
      total += item.preco;
      let linha = `
          <div class="cart-item">
            <img src="${item.imagem}" alt="${item.nome}" class="cart-item__img" />

            <div class="cart-item__content">
              <h3 class="cart-item__name">${item.nome}</h3>
              <p class="cart-item__price">R$ ${item.preco.toFixed(2)}</p>
            </div>

            <button class="cart-item__remove" aria-label="Remover ${item.nome}">
              ✕
            </button>
          </div>`
          // Atualizando total (tofixed para arredonda para dois numeros dps da virgula))
          document.querySelector("#cart-total").innerText = total.toFixed(2);

      carrinho.innerHTML += linha;

    }
  }
}

mostrar_carrinho();