function LoadingDisplay({ cardClass }) {
  return (
    <div className={`${cardClass} flex flex-col items-center justify-center px-10 py-8 text-xl`}>
      <span className="opacity-50 text-2xl font-medium mb-5">Loading</span>
      <span className="loading loading-spinner loading-xl"></span>
    </div>
  )
}

export default LoadingDisplay;
