function Price({price}) {
  return (
      <div className="short-price-row">
        <p>{price.name}</p>
        <p>{price.value} руб.</p>
      </div>
  );
}

function PricesList({prices, category, kind, subKind=[null]}) {
  return (prices.map(price => {
    if (price['equipmentCategory'] === category
        && kind.includes(price.repairKind.name)
        && subKind.includes(price.repairSubkind.name))
    {
      return <Price key={price.id} price={price}/>
    }
    return null
  }))
}

export default PricesList