function NoDataDisplay({ cardClass, year }) {
  return (
    <div className={`${cardClass} flex flex-col items-center justify-center px-10 py-8 text-xl`}>
      <span className="text-2xl font-semibold mb-5">{year}</span>
      <span className="opacity-50 text-3xl">No Data</span>
    </div>
  )
}

export default NoDataDisplay;
